# enes100.py  (pseudocode)

# A simplified conceptual version of the ENES100 Micropython library
# used to connect an ESP32 to the ENES100 Vision System.

class ENES100:
    # ==============================
    # Initialization and Setup
    # ==============================

    def __init__(self):
        self.team_name = ""
        self.team_type = ""
        self.aruco_id = -1
        self.room_num = 0

        self.x = -1.0          # X coordinate from vision system
        self.y = -1.0          # Y coordinate from vision system
        self.theta = -1.0      # Orientation (radians)
        self.is_visible = False

        self.connected = False # Connection status

    # ------------------------------
    # Establish connection
    # ------------------------------
    def begin(self, team_name: str, team_type: str, aruco_id: int, room_num: int):
        """
        Connects ESP32 to the ENES100 Vision System over WiFi.
        Registers the team name, mission type, and ArUco marker.
        """
        self.team_name = team_name
        self.team_type = team_type
        self.aruco_id = aruco_id
        self.room_num = room_num

        # Try to connect to Vision System server
        self.connected = self._connect_wifi()
        while not self.connected:
            wait(0.5)
            self.connected = self._connect_wifi()

        return self.connected

    def _connect_wifi(self):
        # Low-level function to handle WiFi connection and handshake
        # Returns True if the Vision System acknowledges the team
        pass


    # ==============================
    # Vision System Data
    # ==============================

    def update_pose(self):
        """
        Requests the latest x, y, theta, and visibility data
        from the Vision System and updates local variables.
        """
        # Communication with Vision System happens here
        # Values are updated via JSON or socket message
        self.x = get_latest_value("x")
        self.y = get_latest_value("y")
        self.theta = get_latest_value("theta")
        self.is_visible = get_latest_value("visible")

    # Helper properties (for direct attribute access)
    @property
    def x(self):
        self.update_pose()
        return self._x

    @property
    def y(self):
        self.update_pose()
        return self._y

    @property
    def theta(self):
        self.update_pose()
        return self._theta

    @property
    def is_visible(self):
        self.update_pose()
        return self._visible


    # ==============================
    # Status Checks
    # ==============================

    def is_connected(self):
        """
        Returns True if ESP32 is still connected to Vision System.
        """
        return self.connected


    # ==============================
    # Communication / Debugging
    # ==============================

    def print(self, message: str):
        """
        Sends a text message to the Vision System console.
        Used for debugging only.
        """
        if self.connected:
            send_to_server("PRINT", message)


    # ==============================
    # Mission Reporting
    # ==============================

    def mission(self, type: str, message):
        """
        Sends a mission result to the Vision System.
        Example:
            mission('WEIGHT', 'HEAVY')
            mission('NUM_CANDLES', 3)
        """
        if self.connected:
            send_to_server("MISSION", {"type": type, "value": message})


# ==============================
# Example Usage
# ==============================

# Create instance
enes100 = ENES100()

# Initialize connection
enes100.begin("TeamMars", "DATA", 12, 1116)

# Check connection
if enes100.is_connected():
    enes100.print("Connected successfully!")

# Get marker position
print(enes100.x, enes100.y, enes100.theta)

# Send mission result (for DATA team)
enes100.mission("MAGNETISM", "MAGNETIC")
