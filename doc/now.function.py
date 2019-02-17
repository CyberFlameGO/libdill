
fxs.append(
    {
        "name": "now",
        "section": "Deadlines",
        "info": "get current time",
        "result": {
            "type": "int64_t",
            "info": "Current time."
        },
        "args": [
        ],

        "prologue": """
            Returns current time, in milliseconds.

            The function is meant for creating deadlines. For example, a point
            of time one second from now can be expressed as **now() + 1000**.

            The following values have special meaning and cannot be returned by
            the "function":

            * 0: Immediate deadline.
            * -1: Infinite deadline.
        """,

        "example": """
            int result = chrecv(ch, &val, sizeof(val), now() + 1000);
            if(result == -1 && errno == ETIMEDOUT) {
                printf("One second elapsed without receiving a message.\\n");
            }
        """,
    }
)