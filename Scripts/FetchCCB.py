from PIL import Image, ImageDraw, ImageFont


def main():
    # chars, width, height
    data = [
        ["专业丛东丝丢两严丧个丰临为丽举么义乌乐乒乓乔乖乘习乡书买于亏亚产亩亲仓众伞兔兰关兴养兽冈册军农冤凤凭凳击剪劈办务劳势匀匆华单卖卡卫卷厂厅历厉压厌厕厦县发变叠另吞启吴员咸哥哭售囊团园围图圆圈圣坚垄垒垦垫堡壳壶处备复头夸夹夺奋奖姜孕宁它实审宪宫宽宾寇寨寻导尘尝层岁岂岔岗岛崭已币帘带帮并广庆库应庙废开异弃弯录态怎总恳恶您悬惠惩愿截户扁拜拿摇攀敌敲旁无旱显晓晕晨暂术朵杀杂杰枣查桌桨梦步每毕毙毫毯气氧浆灭灵灾烫热爬爱爷爸爹牵犁狱瓣甩电疆疗疤疮疯疼痒痰瘦皂盏盐监盒盖盘离秃穷窑窗窜窝竖竞竟笋笔笨笼筐筛筝筹签简箩篮类粪粱紧絮继网罗罚罢罩羞羡翅耍聋聚肃肾臂舅舍艺节芒芬苍苏苹范茧茫荐荡荣药莲获菠萍萝营蓝蔬藏虏虑虽蠢衔袭裹见览觉贝贞负贡责贤货质贪贫贯贵贷贸费贺资赏赛赞赢赵赶趁趋趟车轰载辈辜辨辩辫边辽达迁过迈运还这进远违连迟迹适选递遗邀酱鉴铅长门闪闭问闯闲间闷闸闹闻阀阁阅阔隶雹雾霉霸靠页题风饰马驾骂鱼鲁鸟鹰黎黑齐齿龙龟",
         20, 21],
        ["丐丫亢仑俞兑兹冀冉冕凫凰凿刁匈匕匣匾卉卞卢卤厢叁吕吝呐咎咒咨噩嚣囤囱坠堑墅壹夭夯奎奕奠奢娄娶婪婴孪孽宠宦寐寞寥尔尧尬尴尹屁屉屎屏岿峦崔嵌巅巍巢巫帚帛幂庐庞廖彝忿怂恿惫憋憨戈戌戍挚挛掣掰摹擎斋昙曰曼柒柬棠樊歹毋毖毡氖氛氟氢氦氨氮氯氰汞泵炙焉煞熏熙熬玫瑟瑶璧瓮瓷甭甸疙疚疟疡疥疵疽痈痉痊痞痪痹瘁瘟瘤瘩瘪瘫瘴瘸瘾癞癣癸皋盂盅盎盔眷矗矣磊祟禀禹秉窍窖窘窥窿笆笙笤笺筷箍箫篆篓篙篡篱篷簇簧粤糜紊罕羌羔羹翘翟耸聂臀舀舆艾芍芜苇苞苟苯茁茉茬茴茵茹荔荚荞荠荤荧荫荸莆莉莎莹莺莽菇菏菲萤萧萨葫蒂蒿蓖蓟蔗蔡蔫蔷蔼蕴蕾薇薛藉藐藕蘑蘸虱蛊蛰蜀蜕衙袁裔裴襄觅詹誊譬豢贰贾赁赘赣迢迪迸逊逛逞逻逾遏闰闺闽阂阉阎阐阑隋雍雳霄霍霎霓霖霹靡韦韭颖鬃鬓鲨鳖鸯鸳龚", 18, 18]
    ]

    for i in range(0, len(data)):
        chars = data[i][0] + " "

        widthOfChars = data[i][1]
        heightOfChars = data[i][2]
        image = Image.open(f"../Data/Chaochaobiao/{i+1}.png")
        for i in range(0, widthOfChars):
            for j in range(0, heightOfChars):
                bigX, bigY = i * 20 + 8, j * 20
                smallX, smallY = i * 20 + 1, j * 20 + 11
                charID = i * heightOfChars + j

                if charID >= len(chars):
                    charID = len(chars) - 1
                cropped = image.crop((i * 20 + 8, j * 20 + 12,
                                      i * 20 + 20, j * 20 + 20))

                encoding = ord(chars[charID])

                unicodeName = f"u{hex(encoding)[2:]}"

                cropped.save(f"../Output/Glyphs/{unicodeName}.png")


if __name__ == "__main__":
    main()
