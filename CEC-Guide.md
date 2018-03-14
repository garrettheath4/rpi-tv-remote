CEC Utilities
=============


Installation
------------

```
sudo apt-get update && sudo apt-get install libcec cec-utils
```


Usage
-----

* Scan for CEC devices connected to Raspberry Pi through its HDMI port

        echo 'scan' | cec-client RPI --single-command --log-level 1

    * The Raspberry Pi will likely be listed with the following device information. Make note of the device type (e.g. `Recorder 1`) and physical address (e.g. `1.0.0.0`) and select that as the "source" when using the [CEC-O-MATIC] website (see below).

        | Field       | Value       |
        |-------------|-------------|
        | vendor      | Pulse Eight |
        | osd string  | CECTester   |
        | CEC version | 1.4         |

* Make the Raspberry Pi the active source on the TV

        echo 'as' | cec-client RPI --single-command --log-level 1

* Make the Raspberry Pi the _inactive_ source on the TV

        echo 'is' | cec-client RPI --single-command --log-level 1

* Send a custom CEC "frame" (i.e. message) from the Raspberry Pi to another connected CEC device

        echo 'tx 1F:82:00:00' | cec-client RPI --single-command --log-level 1

    * **Note:** Use the [CEC-O-MATIC] website to generate a CEC frame with the desired command and use that frame in place of `1F:82:00:00` above.

Reference
---------

* [Using cec-client on a Raspberry Pi][gordonturner] by Gordon Turner
* [CEC-O-MATIC] web tool for creating custom CEC "frame" messages



<!-- Links -->
[gordonturner]: https://blog.gordonturner.com/2016/12/14/using-cec-client-on-a-raspberry-pi/
[CEC-O-MATIC]: http://www.cec-o-matic.com/