def main():
    file = input("File name? ").strip().lower()
    print(MIME_type(file))


def MIME_type(file):
    match file.split('.')[-1]:
        case 'gif':
            return "image/gif"
        case 'jpg' | 'jpeg':
            return "image/jpeg"
        case 'png':
            return "image/png"
        case 'pdf':
            return "application/pdf"
        case 'txt':
            return "text/plain"
        case 'zip':
            return "application/zip"
        case _:
            return "application/octet-stream"


main()
