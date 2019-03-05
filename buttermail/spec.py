import pluggy

hookspec = pluggy.HookspecMarker('buttermail')


@hookspec
def set_header(message, key, value):
    return message, key, value
