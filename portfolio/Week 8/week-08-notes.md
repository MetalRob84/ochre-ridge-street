# Fix Test #
duckie@duckyulon:~$ sudo i2cdetect -y -r 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
40: -- 41 -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: 60 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                        

duckie@duckyulon:~$ docker logs driver-wheels --tail 20
User configuration file found. Loading configuration from /data/config/node/wheels_driver_base/duckyulon.yaml
[DaguWheelsDriver] Running in configuration `DB19`, using driver `HATv2`
[DaguWheelsDriver] Motor #1: Motor[name=left, in1=9, in2=10, pwm=8, controller=PWMMotorDirectionController[in1=9, in2=10]]
[DaguWheelsDriver] Motor #2: Motor[name=right, in1=12, in2=11, pwm=13, controller=PWMMotorDirectionController[in1=12, in2=11]]
2026-10-16 03:03:32 duckyulon dtps_http.self[1] INFO Starting clock dtps/clock/ with interval 1.0
2026-10-16 03:03:32 duckyulon dtps_http[1] INFO Starting TCP server - the URL is 'http://0.0.0.0:40203/'
2026-10-16 03:03:32 duckyulon dtps_http[1] INFO starting Unix server on path /dtps/node/wheels_driver_base.sock
2026-10-16 03:03:32 duckyulon dtps_http[1] INFO starting Unix server on path /tmp/dtps-self-6fa67564
2026-10-16 03:03:32 duckyulon dtps_http[1] INFO available URLs
* http://172.20.24.45:40203/
* http://172.17.0.1:40203/
* http://duckyulon:40203/
* http+unix://%2Fdtps%2Fnode%2Fwheels_driver_base.sock/
* http+unix://%2Ftmp%2Fdtps-self-6fa67564/

2026-10-16 03:03:33 duckyulon dtps-passthrough[1] INFO Configuring passthrough...
2026-10-16 03:03:34 duckyulon dtps-passthrough[1] INFO Passthrough configured.
2026-10-16 03:03:34 duckyulon dtps-passthrough[1] INFO Starting passthrough...
2026-10-16 03:03:34 duckyulon dtps-passthrough[1] INFO No destination to publish to. Remaining idle.
2026-10-16 03:03:37 duckyulon wheels_driver_base[1] INFO Emergency Stop Released

duckie@duckyulon:~$ docker logs driver-display --tail 20
2026-10-16 01:54:34 duckyulon dtps_http[51] INFO starting Unix server on path /tmp/dtps-self-288af618
2026-10-16 01:54:34 duckyulon dtps_http[51] INFO available URLs
* http://172.20.24.45:46019/
* http://172.17.0.1:46019/
* http://duckyulon:46019/
* http+unix://%2Fdtps%2Fnode%2Fdisplay_driver_interaction_plate.sock/
* http+unix://%2Ftmp%2Fdtps-self-288af618/

2026-10-16 01:54:50 duckyulon dtps_http.self[52] INFO Starting clock dtps/clock/ with interval 1.0
2026-10-16 01:54:50 duckyulon dtps_http[52] INFO Starting TCP server - the URL is 'http://0.0.0.0:33265/'
2026-10-16 01:54:50 duckyulon dtps_http[52] INFO starting Unix server on path /dtps/node/display_renderer.sock
2026-10-16 01:54:50 duckyulon dtps_http[52] INFO starting Unix server on path /tmp/dtps-self-f462c187
2026-10-16 01:54:50 duckyulon dtps_http[52] INFO available URLs
* http://172.20.24.45:33265/
* http://172.17.0.1:33265/
* http://duckyulon:33265/
* http+unix://%2Fdtps%2Fnode%2Fdisplay_renderer.sock/
* http+unix://%2Ftmp%2Fdtps-self-f462c187/

<== App terminated!

- Both wheels move same direction.
- Oled displays information.

# Camera Observations #
## 1 ##
Wide lens, distorted, very fish eyed. Could cause the bot to "think" that objects are too far/close.
The reason calibrations are necessary, to compensate for the distortions, camera angle.

## 2 ##
Max frame rate is 30 fps. Low latency, skipping. But that would only affect the camera feed to the PC, it wont affect what the bot sees.
Too many frames could be too much information and overload the processor... But unlikely.

## 3 ##
Low quality, washed out, grainy. Wont cause too much issues, bot only really sees in b&w. 
If quality is too low, or out of focus, the bot could get confused by what it sees.
