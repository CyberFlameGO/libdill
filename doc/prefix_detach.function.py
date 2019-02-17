
fxs.append(
    {
        "name": "prefix_detach",
        "info": "terminates PREFIX protocol and returns the underlying socket",
        "result": {
            "type": "int",
            "success": "underlying socket handle",
            "error": "-1",
        },
        "args": [
           {
               "name": "s",
               "type": "int",
               "info": "Handle of the PREFIX socket.",
           },
        ],
        "protocol": prefix_protocol,
        "prologue": """
            This function does the terminal handshake and returns underlying
            socket to the user. The socket is closed even in the case of error.
        """,

        "has_handle_argument": True,
        "has_deadline": True,
        "uses_connection": True,

        "custom_errors": {
            "ENOTSUP": "The handle is not a PREFIX protocol handle.",
        },
    }
)