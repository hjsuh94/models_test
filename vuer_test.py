import numpy as np
from asyncio import sleep

from vuer import Vuer, VuerSession
from vuer.schemas import Urdf

app = Vuer()
# Untoggle to enable remote connections from AVP.
# app = Vuer(host='0.0.0.0', cert="cert.pem", key="key.pem")

@app.spawn(start=True)
async def main(app: VuerSession):
    i = 0
    while True:
        app.upsert @ Urdf(
            src="https://raw.githubusercontent.com/hjsuh94/models_test/main/box.urdf",
            key="robot",
            # Note that X_WVuerBox = X_WVuerWDrake @ X_WDrakeBox.
            # We need to transform drom Drake's configurations accordingly for
            # correct visualization.
            position=[0.05 * np.cos(0.05 * i),
                      0.1 +  0.05 * np.sin(0.05 * i), 
                      0.0],
            rotation=[0, 0, np.pi/2]
        )
        await sleep(0.01)
        i += 1
