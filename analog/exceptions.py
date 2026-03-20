class UnknownLogKind(ValueError):
    """Exception thrown when an unknown ``kind`` is passed."""

    def __init__(self, value):
        """
        Construct the exception.

        :param value: The invalid kind value passed in.
        """
        super().__init__(f"Unknown log entry kind {value!r}")


class NoExtraField(ValueError):
    pass
