#!/usr/bin/env python3

from FileDownloader import FileDownloader
import argparse

def main(fileURL, filePath):
    fileDownloader = FileDownloader(fileURL, filePath) 
    fileDownloader.start()

def arg_parser():
    parser = argparse.ArgumentParser(description="FDM, Free Download Manager", prog='PROG')
    parser.add_argument("-u", "--url", help="url for download")
    parser.add_argument("-p", "--path", help="path for save file")
    return parser

if __name__ == "__main__":
    parser = arg_parser()
    arg = parser.parse_args()

    if not arg.url or not arg.path:
       parser.print_help()
       exit(-1)

    main(arg.url, arg.path)

    
