from textnode import *

def main():
    testNode = TextNode("sample anchor text", TextType.LINK, "https:www.google.com")
    print(testNode)

if __name__ == "__main__":
    main()