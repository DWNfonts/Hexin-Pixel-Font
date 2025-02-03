from PIL import Image, ImageDraw, ImageFont


def main():
    chars = "专业丛东丝丢两严丧个丰临为丽举么义乌乐乒乓乔乖乘习乡书买于亏亚产亩亲仓众伞兔兰关兴养兽冈册军农冤凤凭凳击剪劈办务劳势匀匆华单卖卡卫卷厂厅历厉压厌厕厦县发变叠另吞启吴员咸哥哭售囊团园围图圆圈圣坚垄垒垦垫堡壳壶处备复头夸夹夺奋奖姜孕宁它实审宪宫宽宾寇寨寻导尘尝层岁岂岔岗岛崭已币帘带帮并广庆库应庙废开异弃弯录态怎总恳恶您悬惠惩愿截户扁拜拿摇攀敌敲旁无旱显晓晕晨暂术朵杀杂杰枣查桌桨梦步每毕毙毫毯气氧浆灭灵灾烫热爬爱爷爸爹牵犁狱瓣甩电疆疗疤疮疯疼痒痰瘦皂盏盐监盒盖盘离秃穷窑窗窜窝竖竞竟笋笔笨笼筐筛筝筹签简箩篮类粪粱紧絮继网罗罚罢罩羞羡翅耍聋聚肃肾臂舅舍艺节芒芬苍苏苹范茧茫荐荡荣药莲获菠萍萝营蓝蔬藏虏虑虽蠢衔袭裹见览觉贝贞负贡责贤货质贪贫贯贵贷贸费贺资赏赛赞赢赵赶趁趋趟车轰载辈辜辨辩辫边辽达迁过迈运还这进远违连迟迹适选递遗邀酱鉴铅长门闪闭问闯闲间闷闸闹闻阀阁阅阔隶雹雾霉霸靠页题风饰马驾骂鱼鲁鸟鹰黎黑齐齿龙龟"
    chars += " "

    widthOfChars = 20
    heightOfChars = 21
    image = Image.new("RGBA", (widthOfChars * 20, heightOfChars * 20))
    draw = ImageDraw.Draw(image)
    bigFont = ImageFont.truetype("../Data/Fonts/Style Reference.otf", 12)
    smallFont = ImageFont.truetype("../Data/Fonts/Fallback Components.otf", 8)

    bigColor = (0, 0, 0)
    smallColor = (0, 0, 0)
    glyphBgColor = (255, 255, 255)
    bgColor = (127, 127, 127)

    draw.rectangle(
        ((0, 0), (widthOfChars * 20 - 1, heightOfChars * 20 - 1)), fill=bgColor)
    for i in range(0, widthOfChars):
        for j in range(0, heightOfChars):
            bigX, bigY = i * 20 + 8, j * 20
            smallX, smallY = i * 20 + 1, j * 20 + 11
            charID = i * heightOfChars + j

            if charID >= len(chars):
                charID = len(chars) - 1

            draw.text((bigX, bigY), chars[charID], bigColor, font=bigFont)
            draw.text((smallX, smallY),
                      chars[charID], smallColor, font=smallFont)
            draw.rectangle(((i * 20 + 8, j * 20 + 12),
                           (i * 20 + 19, j * 20 + 18)), fill=glyphBgColor)

    image.save("../Output/Scaffold.png")


if __name__ == "__main__":
    main()
