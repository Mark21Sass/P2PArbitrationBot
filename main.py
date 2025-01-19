import nodriver as uc
from src.login_and_savecookie import login_and_savecookie
from time import sleep

async def main():
    await login_and_savecookie('marksass2109@icloud.com', 'M1A2rik.')

if __name__ == '__main__':
    uc.loop().run_until_complete(main())

