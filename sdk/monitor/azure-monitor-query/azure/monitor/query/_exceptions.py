#
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
from typing import Any, List, Optional

from ._models import LogsQueryStatus

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # pylint: disable=ungrouped-imports


JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class LogsQueryError:
    """The code and message for an error."""

    code: str
    """A machine readable error code."""
    message: str
    """A human readable error message."""
    details: Optional[List[JSON]] = None
    """A list of additional details about the error."""
    status: LogsQueryStatus
    """Status for error item when iterating over list of results. Always "Failure" for an instance of a
    LogsQueryError."""

    def __init__(self, **kwargs: Any) -> None:
        self.code = kwargs.get("code", "")
        self.message = kwargs.get("message", "")
        self.details = kwargs.get("details", None)
        self.status = LogsQueryStatus.FAILURE

    def __str__(self) -> str:
        return str(self.__dict__)

    @classmethod
    def _from_generated(cls, generated):
        if not generated:
            return None
        innererror = generated
        while innererror.get("innererror"):
            innererror = innererror["innererror"]
        message = innererror.get("message")
        return cls(
            code=generated.get("code"),
            message=message,
            details=generated.get("details"),
        )
