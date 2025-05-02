import re
from db.db import  increment_word
    
async def word_counter(message):
    nigga_words = [ "nigger", "niggers", "niggi", "nigg", "niga", "nga", "nick gurr", "nyaka" ]
    
    if message.content.lower().endswith("ni"):
        count = increment_word("nigga")
        await message.channel.send(f"📈 The word nigga w l'chabibet has now been said {count} times!", delete_after=3)
        
    for word in nigga_words:
        pattern = r"\b" + re.escape(word) + r"\b"
        if re.search(pattern, message.content, re.IGNORECASE) and "m3alim" not in message.content:
            count = increment_word("nigga")
            await message.channel.send(f"📈 The word nigga w l'chabibet has now been said {count} times!", delete_after=3)

    tracked_words = ["haerin", "chaewon", "chabeb", "based", "cho", "nigga"]
    for word in tracked_words:
        pattern = r"\b" + re.escape(word) + r"\b"
        if re.search(pattern, message.content, re.IGNORECASE) and "m3alim" not in message.content:
            count = increment_word(word)
            await message.channel.send(f"📈 The word {word} has now been said {count} times!", delete_after=3)