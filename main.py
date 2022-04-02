import discord
from discord.ext import commands
from datetime import datetime as dt

import mealfind as mf


app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name)
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def meal(ctx):
    t_m, t_d= dt.today().strftime("%m"), dt.today().strftime("%d")
    
    meal_data = mf.mealfind.find(0)
    
    embed=discord.Embed(title="~ 중 식 ~", description=t_m+ "월 "+t_d+" 일", color=0xff7024)
    if(meal_data[0][0]=="None"):
        embed.add_field(name = "없음", value = "급식 혹은 급식 정보가 없음",inline=False)
    else:
        for i,j in meal_data[0]:
            if j=="":
                j="없음"
            embed.add_field(name = i, value= j, inline=False)
    await ctx.send(embed=embed)
        

    embed=discord.Embed(title="~ 석 식 ~", description=t_m+ "월 "+t_d+" 일", color=0xff8888)
    if(meal_data[1][0]=="None"):
        embed.add_field(name = "없음", value = "급식 혹은 급식 정보가 없음",inline=False)
    else:
        for i,j in meal_data[1]:
            if j=="":
                j="없음"
            embed.add_field(name = i, value = j, inline=False)
    await ctx.send(embed=embed)

@app.command()
async def lotto(ctx):
    await ctx.send("꽝")



app.run('OTU5ODE2NjgzMjY1MDczMjIz.YkhY8Q.h2VpLsm87NMRZnUVDlE-m0xek5k')