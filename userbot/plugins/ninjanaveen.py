"""Emoji
Available Commands:
.ninjanaveen
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("ninjanaveen"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ninjanaveen":
    await event.edit("@ninjanaveen")
    animation_chars = [
            "@ninjanaveen is a Pro",
            "@ninjanaveen is a Cracker",
            "@ninjanaveen is in love with Biology Practicals",
            "@ninjanaveen is The Creator of @NinjaHunter",
            "@ninjanaveen is the Owner of @Royal_Giveaway",
            "@ninjanaveen is the Owner of @ConfigsByNinja",
            "Give Him Biology Practicals else Gey!"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
