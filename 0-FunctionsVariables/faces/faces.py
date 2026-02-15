def convert(message):
    return message.replace(":)", "😊").replace(":(", "☹️")


def main():
    message = input("What's your message?")
    print(convert(message))

    main()
