REMOTE_LOGGING_STATUS_SCM = 1


def enable_disable_remote_logging(status):
    global REMOTE_LOGGING_STATUS_SCM
    text = ("disabled", "enabled")[status]
    if REMOTE_LOGGING_STATUS_SCM == status:
        print("remote logging already " + text)
    else:
        print(text + " the remote log server")
        REMOTE_LOGGING_STATUS_SCM = status


enable_disable_remote_logging(1)
enable_disable_remote_logging(0)
enable_disable_remote_logging(1)

# print(("Off", "On")[1])