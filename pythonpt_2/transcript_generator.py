import sys

def transcript_generator(STRING_id):
    from youtube_transcript_api import YouTubeTranscriptApi
    from docx import Document
    transcript = YouTubeTranscriptApi.get_transcript(STRING_id)
    doc = Document()
    for t in transcript:
        doc.add_paragraph(t["text"].strip())
    doc.save('demo' + str(STRING_id) + '.docx')
    return doc

transcript_generator(str(sys.argv[1]))
    