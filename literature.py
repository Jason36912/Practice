from docx import Document
import docx
def get_docx(filename):
    d = docx.Document(filename)
    return d
i = 0
doc = get_docx('E:\\植保srt\\2019读书报告\\尾注序号.docx')
for paragraph in doc.paragraphs:
    paragraph.text.replace('[ ]','[1]')
    print(paragraph.text)
