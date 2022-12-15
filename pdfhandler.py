import pikepdf
from pathlib import Path
from io import BytesIO


class PdfTicketWriter:
    def __init__(self, blank_ticket_path: Path|str) -> None:
        # open the file and read in the first page
        self.blank_ticket_path = Path(blank_ticket_path)
        self.pdf_bytes = BytesIO(self.blank_ticket_path.read_bytes())
        self.pdf = None
        self.page = None
        self.instructions = None
        self.is_ready = True
        self.reload()

    def reload(self) -> None:
        """
        Reloads the pikepdf object from the PDF bytes.
        """
        self.pdf_bytes.seek(0)
        self.pdf = pikepdf.open(self.pdf_bytes)
        self.page = self.pdf.pages[0]
        self.instructions = pikepdf.parse_content_stream(self.page)
        self.add_courier

    def add_courier(self) -> None:
        """
        Adds a reference to the Courier font to the PDF.
        """
        if pikepdf.Name.Courier in self.page.resources.Font:
            return

        # add an indirect reference to one of the standard 11 fonts.
        courier = pikepdf.Dictionary(
            Type=pikepdf.Name.Font,
            Subtype=pikepdf.Name.Type1,
            BaseFont=pikepdf.Name.Courier,
            Name=pikepdf.Name.Courier,
        )

        self.pdf.make_indirect(courier)
        self.page.add_resource(courier, pikepdf.Name.Font, '/Courier')

    def make_text_instructions(self, text: str, x: float, y: float, size: float=9.0) -> list[pikepdf.ContentStreamInstruction]:
        """
        Creates list of low-level PDF instructions to add `text` at page
        location `x`, `y`, with font size of `size`.
        """
        CSI = pikepdf.ContentStreamInstruction


        instructions = [
            CSI([], pikepdf.Operation('BT')),   # begin text
            CSI([pikepdf.Name.Courier, size], pikepdf.Operator('Tf')),  # set font
            CSI([1,0,0,1,x,y], pikepdf.Operator('Tm')),     # move cursor to x, y
            CSI([pikepdf.String(text)], pikepdf.Operator('Tj')),    # paint text
            CSI([], pikepdf.Operation('ET')),   # end text
        ]
        return instructions


    def insert_instructions(self, 
                            new_instructions: list[pikepdf.ContentStreamInstruction]
                            ) -> None:
        """
        Inserts the new set of instructions after the last ENDTEXT instruction.
        """
        ix = 0
        for i, (_, op) in enumerate(self.instructions):
            if str(op) == 'ET':
                ix = i
        self.instructions = [
            *self.instructions[:ix], 
            *new_instructions, 
            *self.instructions[ix:]
        ]
        # the pdf is not ready until the content stream is written
        self.is_ready = False


    def set_content_stream(self) -> None:
        """
        Sets the content stream of the page to the current set of instructions.
        """
        content_stream = pikepdf.unparse_content_stream(self.instructions)
        self.page.Contents = self.pdf.make_stream(content_stream)
        self.is_ready = True


    def add_text(self, text: str, x: float, y: float, size: float=9.0) -> None:
        """
        Adds the text at x, y and sets the content stream.
        """
        instr = self.make_text_instructions(text, x, y, size)
        self.insert_instructions(instr)
        self.set_content_stream()


    def to_bytesio(self) -> BytesIO:
        """
        Returns a BytesIO object of the modified PDF, if it is ready.
        """
        if not self.is_ready:
            raise BufferError('The content stream of the modified PDF has '
                'not been set, use `.set_content_stream`')

        fp_out = BytesIO()
        self.pdf.save(fp_out)
        fp_out.seek(0)
        return fp_out
