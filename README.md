
## Installation 

```bash

python3 -m venv venv 

source venv/bin/activate

pip install -r requirements.txt

``` 


## Register 

`python3 register.py` 

1. Follow the prompts. 
1. Copy the API key
1. Save API key in `.env-example` 
1. Delete instructions in `.env` file
1. Rename `.env-example` to `.env`


## Run 

`python3 cli-control.py`

1. List all lights
2. Choose active light
3. Turn on active light
4. Change light color (prompt hex value)
5. Turn off active light
6. Exit the appgit


## License

This project is licensed under the MIT License. This means:

- You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
- You must include the original copyright notice and a copy of the license in any substantial portions of the Software.
- The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

For more details, please visit [Open Source Initiative](https://opensource.org/license/mit).

