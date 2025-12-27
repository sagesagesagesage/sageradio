import time

class CDTimer:
    def __init__(self):
        self._initial_start_time = None  # first-ever start timestamp
        self._end_time = None            # current end timestamp
        self._duration = None            # original duration (seconds)

    def start(self, seconds: float):
        """Start the countdown for `seconds`. Records the original start time once."""
        if seconds <= 0:
            raise ValueError("Seconds must be greater than zero.")
        self._duration = float(seconds)
        now = time.time()
        self._end_time = now + self._duration
        if self._initial_start_time is None:
            self._initial_start_time = now

    def restart(self):
        """
        Restart the countdown using the original duration.
        The original start time is preserved for `elapsed()`.
        """
        if self._duration is None:
            raise RuntimeError("Timer has not been started yet.")
        self._end_time = time.time() + self._duration
        # NOTE: _initial_start_time is intentionally NOT changed

    def completed(self) -> bool:
        """Return True if the countdown has completed."""
        if self._end_time is None:
            return False
        return time.time() >= self._end_time

    def remaining(self) -> float:
        """Return seconds remaining (0.0 if not started or already completed)."""
        if self._end_time is None:
            return 0.0

