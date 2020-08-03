import discord
from discord.ext import commands
import wf_pars
import spec_def
import json
from discord import Member
import time

client = commands.Bot(command_prefix = '!')

search_stats = {
    'blackwood_win' : '[difficulty]blackwood [mode]PVE [stat]player_sessions_won',
    'blackwood_lose' : '[difficulty]blackwood [mode]PVE [stat]player_sessions_lost',

    'hydra_win' : '[difficulty]pve_arena [mode]PVE [stat]player_sessions_won',
    'hydra_lose' : '[difficulty]pve_arena [mode]PVE [stat]player_sessions_lost',

    'survivalmission_win' : '[difficulty]survivalmission [mode]PVE [stat]player_sessions_won',
    'survivalmission_lose' : '[difficulty]survivalmission [mode]PVE [stat]player_sessions_lost',

    'mars_easy_win' : '[difficulty]marseasy [mode]PVE [stat]player_sessions_won',
    'mars_easy_lose' : '[difficulty]marseasy [mode]PVE [stat]player_sessions_lost',
    'mars_normal_win' : '[difficulty]marsnormal [mode]PVE [stat]player_sessions_won',
    'mars_normal_lose' : '[difficulty]marsnormal [mode]PVE [stat]player_sessions_lost',
    'mars_hard_win' : '[difficulty]marshard [mode]PVE [stat]player_sessions_won',
    'mars_hard_lose' : '[difficulty]marshard [mode]PVE [stat]player_sessions_lost',

    'volcano_easy_win': '[difficulty]volcanoeasy [mode]PVE [stat]player_sessions_won',
    'volcano_easy_lose': '[difficulty]volcanoeasy [mode]PVE [stat]player_sessions_lost',
    'volcano_nornal_win': '[difficulty]volcanonornal [mode]PVE [stat]player_sessions_won',
    'volcano_nornal_lose': '[difficulty]volcanonornal [mode]PVE [stat]player_sessions_lost',
    'volcano_hard_win': '[difficulty]volcanohard [mode]PVE [stat]player_sessions_won',
    'volcano_hard_lose': '[difficulty]volcanohard [mode]PVE [stat]player_sessions_lost',
    'volcano_survival_win': '[difficulty]volcanosurvival [mode]PVE [stat]player_sessions_won',
    'volcano_survival_lose': '[difficulty]volcanosurvival [mode]PVE [stat]player_sessions_lost',
    
    'edge_win' : '[difficulty]campaignsection1 [mode]PVE [stat]player_sessions_won',
    'edge_lose': '[difficulty]campaignsection1 [mode]PVE [stat]player_sessions_lost',
    'trap_win' : '[difficulty]campaignsection2 [mode]PVE [stat]player_sessions_won',
    'trap_lose' : '[difficulty]campaignsection2 [mode]PVE [stat]player_sessions_lost',
    'summit_win' : '[difficulty]campaignsection3 [mode]PVE [stat]player_sessions_won',
    'summit_lose' : '[difficulty]campaignsection3 [mode]PVE [stat]player_sessions_lost',
    'marathon_win' : '[difficulty]campaignsections [mode]PVE [stat]player_sessions_won',
    'marathon_lose' : '[difficulty]campaignsections [mode]PVE [stat]player_sessions_lost',

    'zombie_easy_win' : '[difficulty]zombieeasy [mode]PVE [stat]player_sessions_won',
    'zombie_easy_lose' : '[difficulty]zombieeasy [mode]PVE [stat]player_sessions_lost',
    'zombie_normal_win' : '[difficulty]zombienormal [mode]PVE [stat]player_sessions_won',
    'zombie_normal_lose' : '[difficulty]zombienormal [mode]PVE [stat]player_sessions_lost',
    'zombie_hard_win' : '[difficulty]zombiehard [mode]PVE [stat]player_sessions_won',
    'zombie_hard_lose' : '[difficulty]zombiehard [mode]PVE [stat]player_sessions_lost',

    'anubis_easy_win' : '[difficulty]anubiseasy [mode]PVE [stat]player_sessions_won',
    'anubis_easy_lose' : '[difficulty]anubiseasy [mode]PVE [stat]player_sessions_lost',
    'anubis_normal_win' : '[difficulty]anubisnormal [mode]PVE [stat]player_sessions_won',
    'anubis_normal_lose' : '[difficulty]anubisnormal [mode]PVE [stat]player_sessions_lost',
    'anubis_hard_win' : '[difficulty]anubishard [mode]PVE [stat]player_sessions_won',
    'anubis_hard_lose' : '[difficulty]anubishard [mode]PVE [stat]player_sessions_lost',

    'anubis2_easy_win' : '[difficulty]anubiseasy2 [mode]PVE [stat]player_sessions_won',
    'anubis2_easy_lose' : '[difficulty]anubiseasy2 [mode]PVE [stat]player_sessions_lost',
    'anubis2_normal_win' : '[difficulty]anubisnormal2 [mode]PVE [stat]player_sessions_won',
    'anubis2_normal_lose' : '[difficulty]anubisnormal2 [mode]PVE [stat]player_sessions_lost',
    'anubis2_hard_win' : '[difficulty]anubishard2 [mode]PVE [stat]player_sessions_won',
    'anubis2_hard_lose' : '[difficulty]anubishard2 [mode]PVE [stat]player_sessions_lost',

    'zombietower_easy_win' : '[difficulty]zombietowereasy [mode]PVE [stat]player_sessions_won',
    'zombietower_easy_lose' : '[difficulty]zombietowereasy [mode]PVE [stat]player_sessions_lost',
    'zombietower_normal_win' : '[difficulty]zombietowernormal [mode]PVE [stat]player_sessions_won',
    'zombietower_normal_lose' : '[difficulty]zombietowernormal [mode]PVE [stat]player_sessions_lost',
    'zombietower_hard_win' : '[difficulty]zombietowerhard [mode]PVE [stat]player_sessions_won',
    'zombietower_hard_lose' : '[difficulty]zombietowerhard [mode]PVE [stat]player_sessions_lost',

    'icebreaker_easy_win' : '[difficulty]icebreakereasy [mode]PVE [stat]player_sessions_won',
    'icebreaker_easy_lose' : '[difficulty]icebreakereasy [mode]PVE [stat]player_sessions_lost',
    'icebreaker_normal_win' : '[difficulty]icebreakernormal [mode]PVE [stat]player_sessions_won',
    'icebreaker_normal_lose' : '[difficulty]icebreakernormal [mode]PVE [stat]player_sessions_lost',
    'icebreaker_hard_win' : '[difficulty]icebreakerhard [mode]PVE [stat]player_sessions_won',
    'icebreaker_hard_lose' : '[difficulty]icebreakerhard [mode]PVE [stat]player_sessions_lost',

    'chernobyl_easy_win' : '[difficulty]chernobyleasy [mode]PVE [stat]player_sessions_won',
    'chernobyl_easy_lose' : '[difficulty]chernobyleasy [mode]PVE [stat]player_sessions_lost',
    'chernobyl_normal_win' : '[difficulty]chernobylnormal [mode]PVE [stat]player_sessions_won',
    'chernobyl_normal_lose' : '[difficulty]chernobylnormal [mode]PVE [stat]player_sessions_lost',
    'chernobyl_hard_win' : '[difficulty]chernobylhard [mode]PVE [stat]player_sessions_won',
    'chernobyl_hard_lose' : '[difficulty]chernobylhard [mode]PVE [stat]player_sessions_lost',

    'japan_easy_win' : '[difficulty]japaneasy [mode]PVE [stat]player_sessions_won',
    'japan_easy_lose' : '[difficulty]japaneasy [mode]PVE [stat]player_sessions_lost',
    'japan_normal_win' : '[difficulty]japannormal [mode]PVE [stat]player_sessions_won',
    'japan_normal_lose' : '[difficulty]japannormal [mode]PVE [stat]player_sessions_lost',
    'japan_hard_win' : '[difficulty]japanhard [mode]PVE [stat]player_sessions_won',
    'japan_hard_lose' : '[difficulty]japanhard [mode]PVE [stat]player_sessions_lost',

    'mission_training_win' : '[difficulty]trainingmission [mode]PVE [stat]player_sessions_won',
    'mission_training_lose' : '[difficulty]trainingmission [mode]PVE [stat]player_sessions_lost',
    'mission_easy_win' : '[difficulty]easymission [mode]PVE [stat]player_sessions_won',
    'mission_easy_lose' : '[difficulty]easymission [mode]PVE [stat]player_sessions_lost',
    'mission_normal_win' : '[difficulty]normalmission [mode]PVE [stat]player_sessions_won',
    'mission_normal_lose' : '[difficulty]normalmission [mode]PVE [stat]player_sessions_lost',
    'mission_hard_win' : '[difficulty]hardmission [mode]PVE [stat]player_sessions_won',
    'mission_hard_lose' : '[difficulty]hardmission [mode]PVE [stat]player_sessions_lost'
}

@client.event
async def on_ready():
    print('Bot connected')
    

@client.command(pass_context = True)
async def reg(ctx, nickname):
    result = wf_pars.user_stats(nickname)

    if result == "Пользователь не найден":
        emb = discord.Embed(description="Игрок с таким ником не найден",
        colour=discord.Color.red())
    
    elif result == "Персонаж неактивен":
        emb = discord.Embed(description="Игрок с таким ником давно не заходил в игру",
        colour=discord.Color.red())

    elif result == "Игрок скрыл свою статистику":
        emb = discord.Embed(description="Хочешь чтобы работало - открой статистику ¯\_(ツ)_/¯",
        colour=discord.Color.red())
    
    else:
        to_json = json.load(open('link.json'))

        if nickname in to_json.values():
            emb = discord.Embed(description=f"<@{ctx.message.author.id}>, данный никнейм уже зарестрирован! \n \n Если это ваш аккаунт, свяжитесь с администрацией <@254691314258542593>",
            colour=0x00ff00)

            emb.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
            emb.set_footer(text = client.user.name + " | Обновлено")
            emb.set_thumbnail(url = 'https://i.imgur.com/5psQr0q.jpg')
        else:
            emb = discord.Embed(description=f"<@{ctx.message.author.id}>, Вы успешно зарегестрировались на сервере под ником: " +
            "[" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n \n Теперь Вы можете использовать команду !upd",
            colour=0x00ff00)

            emb.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
            emb.set_footer(text = client.user.name + " | Обновлено")
            emb.set_thumbnail(url = 'https://i.imgur.com/5psQr0q.jpg')

            to_json = json.load(open('link.json'))
            to_json[str(ctx.message.author.id)] = str(nickname)
            with open('link.json', 'w') as f:
                json.dump(to_json, f)

    await ctx.send(embed = emb)

@client.command(pass_context = True)
async def upd(ctx):
    from_json = json.load(open('link.json'))
    try:
        nickname = from_json[str(ctx.message.author.id)]
        result = wf_pars.user_stats(nickname)
    except:
        result = "Не привязан акк"
    

    favoritClassPvE = "Нет"
    favoritClassPvP = "Нет"

    if result == "Пользователь не найден":
        emb = discord.Embed(description="Игрок с таким ником не найден",
        colour=discord.Color.red())
    
    elif result == "Персонаж неактивен":
        emb = discord.Embed(description="Игрок с таким ником давно не заходил в игру",
        colour=discord.Color.red())

    elif result == "Игрок скрыл свою статистику":
        emb = discord.Embed(description="Хочешь чтобы работало - открой статистику ¯\_(ツ)_/¯",
        colour=discord.Color.red())
    elif result == "Не привязан акк":
        emb = discord.Embed(description="Акк не привязан. Пропиши !reg 'Ник'",
        colour=discord.Color.red())
    else:
        if result["server"] == 1:
            server_str = "Альфа"
        elif result["server"] == 2:
            server_str = "Браво"
        elif result["server"] == 3:
            server_str = "Чарли"

        if result["favoritPVP"] == "Recon":
            favoritClassPvP = "Снайпер"
        elif result["favoritPVP"] == "Rifleman":
            favoritClassPvP = "Штурмовик"
        elif result["favoritPVP"] == "Engineer":
            favoritClassPvP = "Инженер"
        elif result["favoritPVP"] == "Medic":
            favoritClassPvP = "Медик"
        elif result["favoritPVP"] == "false":
            favoritClassPvP = "Нет"

        if result["favoritPVE"] == "Recon":
            favoritClassPvE = "Снайпер"
        elif result["favoritPVE"] == "Rifleman":
            favoritClassPvE = "Штурмовик"
        elif result["favoritPVE"] == "Engineer":
            favoritClassPvE = "Инженер"
        elif result["favoritPVE"] == "Medic":
            favoritClassPvE = "Медик"
        elif result["favoritPVE"] == "false":
            favoritClassPvE = "Нет"
        
        emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
        "**Игровой сервер:** " + server_str + "\n" +
        "\n" +
        "**Клан:** " + result["clan_name"] + "\n" +
        "**Ранг:** " + repr(result["rank_id"]) + "\n" +
        "**Время в игре:** " + repr(result["playtime_h"]) + "ч. " + repr(result["playtime_m"]) + "м. \n" +
        "\n" +
        "**• PVP-статистика** \n"
        "> **Убийств**: " + repr(result["kills"]) + "\n" +
        "> **Смертей**: " + repr(result["death"]) + "\n" +
        "> **У/C**: " + repr(result["pvp"]) + "\n" +
        "> **Убийств тиммейтов**: " + repr(result["friendly_kills"]) + "\n" +
        "> **Побед/Поражений**: " + repr(result["pvp_wins"]) + "/" + repr(result["pvp_lost"]) + "\t(" + repr(result["pvp_all"]) + ") \n" +
        "\n" +
        "**• PVE-статистика** \n"
        "> **Убийств**: " + repr(result["pve_kills"]) + "\n" +
        "> **Смертей**: " + repr(result["pve_death"]) + "\n" +
        "> **У/C**: " + repr(result["pve"]) + "\n" +
        "> **Убийств тиммейтов**: " + repr(result["pve_friendly_kills"]) + "\n" +
        "> **Побед/Поражений**: " + repr(result["pve_wins"]) + "/" + repr(result["pve_lost"]) + "\t(" + repr(result["pve_all"]) + ") \n"
        "\n" +
        "**Любимый класс в PVP:** " + favoritClassPvP + "\n" + 
        "**Любимый класс в PVE:** " + favoritClassPvE + "\n"
        ,
        colour=0x00ff00)

        emb.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
        emb.set_footer(text = client.user.name + " | Обновлено", icon_url= client.user.avatar_url)
        emb.set_thumbnail(url = 'https://i.imgur.com/5psQr0q.jpg')

    await ctx.send(embed = emb)

# @client.command(pass_context = True)   Maybe I'll finish it later
# async def online(ctx):
#     sum = 0
#     for member in ctx.guild.members:
#         if str(member.status) == "online" or str(member.status) == "dnd" or str(member.status) == "idle":
#             sum += 1
#     channel = client.get_channel(729927732045021206)
#     await discord.VoiceChannel.edit(channel, name = "Online : " + repr(sum))


@client.command(pass_context = True)
async def help_ru(ctx):
    emb = discord.Embed(description="**!reg** ***никнейм*** - регистрация аккаунта на сервере \n" + 
    "**!upd** - обновление статистики"
    ,
    colour=0x00ff00)

    emb.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
    emb.set_footer(text = client.user.name, icon_url= client.user.avatar_url)
    emb.set_thumbnail(url = 'https://i.imgur.com/5psQr0q.jpg')

    await ctx.send(embed = emb)

@client.command(pass_context = True)
async def spec(ctx, spec_name):
    from_json = json.load(open('link.json'))
    try:
        nickname = from_json[str(ctx.message.author.id)]
        result = wf_pars.user_stats(nickname)
    except:
        result = "Не привязан акк"
    
    if result == "Не привязан акк":
        emb = discord.Embed(description="Акк не привязан. Пропиши !reg 'Ник'",
        colour=discord.Color.red())
    else:
        if result["server"] == 1:
            server_str = "Альфа"
        elif result["server"] == 2:
            server_str = "Браво"
        elif result["server"] == 3:
            server_str = "Чарли"


        if spec_name == "bv" or spec_name == "blackwood" or spec_name == "бв":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Blackwood»** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["blackwood_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["blackwood_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "hydra" or spec_name == "гидра" or spec_name == "hd":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Гидра»** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["hydra_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["hydra_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "elimination" or spec_name == "whiteshark" or spec_name == "ws" or spec_name == "ликва":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Белая Акула»** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["survivalmission_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["survivalmission_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "острие" or spec_name == "остриё" or spec_name == "засада" or spec_name == "марафон" or spec_name == "марафон" or spec_name == "marathon" or spec_name == "бастион":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Снежный Бастион» (Остриё)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["edge_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["edge_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Снежный Бастион» (Засада)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["trap_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["trap_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Снежный Бастион» (Зенит)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["summit_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["summit_lose"])) + "\n"
            "**• Статистика прохождения спецоперации «Снежный Бастион» (Марафон)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["marathon_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["marathon_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "mars" or spec_name == "марс":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Марс» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Марс» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Марс» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mars_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "volcano" or spec_name == "vulcan" or spec_name == "вулкан":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Вулкан» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Вулкан» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Вулкан» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_hard_lose"])) + "\n" +
            "**• Статистика прохождения спецоперации «Вулкан» (Хардкор)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_survival_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["volcano_survival_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "anubis" or spec_name == "анубис":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Анубис» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Анубис» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Анубис» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "anubis2" or spec_name == "затмение":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Затмение» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Затмение» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Затмение» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["anubis2_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "exp" or spec_name == "оэ":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Опасный эксперимент» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Опасный эксперимент» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Опасный эксперимент» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombie_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "blackshark" or spec_name == "ча" or spec_name == "bs":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Чёрная акула» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Чёрная акула» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Чёрная акула» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["zombietower_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "лёд" or spec_name == "ice" or spec_name == "ледокол":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Ледокол» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Ледокол» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Ледокол» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "припять" or spec_name == "chernobyl":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Припять» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Припять» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Припять» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "восход" or spec_name == "japan":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения спецоперации «Восход» (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_easy_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Восход» (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_normal_lose"])) + "\n"+
            "**• Статистика прохождения спецоперации «Восход» (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["icebreaker_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        elif spec_name == "pve" or spec_name == "пве":
            emb = discord.Embed(description="**Игровой ник:** [" + result["nickname"] + "](https://wfts.su/profile/" + nickname + ") \n" +
            "**Игровой сервер:** " + server_str + "\n" +
            "\n" +
            "**• Статистика прохождения миссий (Тренировка)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_training_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_training_lose"])) + "\n"+
            "**• Статистика прохождения миссий (Легко)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_easy_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_easy_lose"])) + "\n"+
            "**• Статистика прохождения миссий (Сложно)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_normal_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_normal_lose"])) + "\n"+
            "**• Статистика прохождения миссий (Профи)** \n" +
            "> **Выполнено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_hard_win"])) + "\n" +
            "> **Провалено:** " + repr(spec_def.spec_one(nickname, result["server"], search_stats["mission_hard_lose"])) + "\n"
            ,colour=0x00ff00)
        else:
            emb = discord.Embed(description="Не верно указана спецоперация. Проверьте написание. !help_ru - помощь"
            ,colour=discord.Color.red())


    emb.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
    emb.set_footer(text = client.user.name, icon_url= client.user.avatar_url)
    emb.set_thumbnail(url = 'https://i.imgur.com/5psQr0q.jpg')
        
    await ctx.send(embed = emb)


token = 'NzIxNzQwMDA0NDYzODY5OTgz.XxhhyQ.xK7td77Plo8Fm6gWSCbrnu3nrBU'

client.run(token)