import nodriver as uc
from time import sleep

async def login_and_savecookie(email, password):
    browser = await uc.start()
    page = await browser.get('https://www.bybit.com/')
    sign_in = await page.select('#HEADER-RIGHT-LOGIN-REGISTER > span.header-login')
    await sign_in.click()

    # input your email
    email_input = await page.select('#uniframe-cht-login > div.by-border-box.cht-justify-center.by-border-radius.by-login-reg-layout > div > div.cht-items-center.by-border-radius.cht-bg-modal-bg.cht-box-border.cht-p-0.cht-flex-1.sm\:cht-mx-\[0px\].by-width > div > div > div:nth-child(2) > div > div > div > form > div.index_by-input-email-newui__mwhRI > div > div.cht-by-input.cht-flex.cht-relative.cht-box-border.cht-w-full.cht-text-sm.cht-transition-colors.cht-ease-in-out.cht-overflow-hidden.cht-border.cht-border-solid.cht-border-error-color > input')
    await email_input.set_value(email)

    # input your password
    password_input = await page.select('#uniframe-cht-login > div.by-border-box.cht-justify-center.by-border-radius.by-login-reg-layout > div > div.cht-items-center.by-border-radius.cht-bg-modal-bg.cht-box-border.cht-p-0.cht-flex-1.sm\:cht-mx-\[0px\].by-width > div > div > div:nth-child(2) > div > div > div > form > div.cht-relative > div > div.cht-by-input.cht-flex.cht-relative.cht-box-border.cht-w-full.cht-text-sm.cht-transition-colors.cht-ease-in-out.cht-overflow-hidden.cht-border.cht-border-solid.cht-border-error-color > input')
    await password_input.set_value(password)

    # continue logining
    confirm = await page.select('#uniframe-cht-login > div.by-border-box.cht-justify-center.by-border-radius.by-login-reg-layout > div > div.cht-items-center.by-border-radius.cht-bg-modal-bg.cht-box-border.cht-p-0.cht-flex-1.sm\:cht-mx-\[0px\].by-width > div > div > div:nth-child(2) > div > div > div > form > button')
    await confirm.click()
    
    sleep(1000)
