#!/usr/bin/env python3
"""Take 5 screenshots of MiMoReadme at 1920x1080 using nodriver."""
import asyncio, nodriver as uc, os

URL = "https://gyoomei.github.io/mimoreadme/index.html"
OUT = os.path.expanduser("~/mimoreadme/screenshots")
os.makedirs(OUT, exist_ok=True)

async def main():
    browser = await uc.start(
        headless=True,
        browser_args=["--no-sandbox", "--disable-gpu"]
    )
    page = await browser.get(URL)
    await page.sleep(2)
    
    # Set viewport 1920x1080
    await page.send(uc.cdp.emulation.set_device_metrics_override(
        width=1920, height=1080, device_scale_factor=1, mobile=False
    ))
    await page.sleep(2)
    
    # 1. Hero/input section (dark)
    await page.save_screenshot(os.path.join(OUT, "01_hero_dark.png"))
    print("✓ Screenshot 1: Hero dark")
    
    # Fill repo URL and description
    try:
        repo_input = await page.select('#repoUrl')
        await repo_input.send_keys("https://github.com/gyoomei/mimogas")
        await page.sleep(0.5)
        desc_input = await page.select('#projectDesc')
        await desc_input.send_keys("Multi-chain gas optimizer with Xiaomi MiMo AI advisor. 15 EVM chains, real-time gas prices, optimization reports.")
        await page.sleep(1)
    except Exception as e:
        print(f"  Input fill note: {e}")
    
    # 2. Input filled
    await page.save_screenshot(os.path.join(OUT, "02_input_filled.png"))
    print("✓ Screenshot 2: Input filled")
    
    # 3. Click generate
    try:
        gen_btn = await page.select('#generateBtn')
        await gen_btn.click()
        await page.sleep(10)  # Wait for API
    except Exception as e:
        print(f"  Generate note: {e}")
    
    # Scroll to output
    await page.evaluate("window.scrollTo(0, 600)")
    await page.sleep(1)
    await page.save_screenshot(os.path.join(OUT, "03_generated_preview.png"))
    print("✓ Screenshot 3: Generated preview")
    
    # 4. Scroll more to see full preview
    await page.evaluate("window.scrollTo(0, 1000)")
    await page.sleep(0.5)
    await page.save_screenshot(os.path.join(OUT, "04_preview_detail.png"))
    print("✓ Screenshot 4: Preview detail")
    
    # 5. Light theme
    await page.evaluate("window.scrollTo(0, 0)")
    await page.sleep(0.5)
    try:
        theme_btn = await page.select('#themeBtn')
        await theme_btn.click()
        await page.sleep(1)
    except:
        pass
    await page.save_screenshot(os.path.join(OUT, "05_light_theme.png"))
    print("✓ Screenshot 5: Light theme")
    
    browser.stop()
    print(f"\n✅ All screenshots saved to {OUT}/")
    for f in sorted(os.listdir(OUT)):
        print(f"  📸 {f}")

asyncio.run(main())
