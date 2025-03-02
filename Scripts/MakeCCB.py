from PIL import Image, ImageDraw, ImageFont


def main():
    chars = "丐丫亢仑俞兑兹冀冉冕凫凰凿刁匈匕匣匾卉卞卢卤厢叁吕吝呐咎咒咨噩嚣囤囱坠堑墅壹夭夯奎奕奠奢娄娶婪婴孪孽宠宦寐寞寥尔尧尬尴尹屁屉屎屏岿峦崔嵌巅巍巢巫帚帛幂庐庞廖彝忿怂恿惫憋憨戈戌戍挚挛掣掰摹擎斋昙曰曼柒柬棠樊歹毋毖毡氖氛氟氢氦氨氮氯氰汞泵炙焉煞熏熙熬玫瑟瑶璧瓮瓷甭甸疙疚疟疡疥疵疽痈痉痊痞痪痹瘁瘟瘤瘩瘪瘫瘴瘸瘾癞癣癸皋盂盅盎盔眷矗矣磊祟禀禹秉窍窖窘窥窿笆笙笤笺筷箍箫篆篓篙篡篱篷簇簧粤糜紊罕羌羔羹翘翟耸聂臀舀舆艾芍芜苇苞苟苯茁茉茬茴茵茹荔荚荞荠荤荧荫荸莆莉莎莹莺莽菇菏菲萤萧萨葫蒂蒿蓖蓟蔗蔡蔫蔷蔼蕴蕾薇薛藉藐藕蘑蘸虱蛊蛰蜀蜕衙袁裔裴襄觅詹誊譬豢贰贾赁赘赣迢迪迸逊逛逞逻逾遏闰闺闽阂阉阎阐阑隋雍雳霄霍霎霓霖霹靡韦韭颖鬃鬓鲨鳖鸯鸳龚"
    chars += " "

    widthOfChars = 18
    heightOfChars = 18
    image = Image.new("RGBA", (widthOfChars * 20, heightOfChars * 20))
    draw = ImageDraw.Draw(image)
    bigFont = ImageFont.truetype("../Data/Fonts/Style Reference.otf", 12)
    smallFont = ImageFont.truetype("../Data/Fonts/Fallback Components.ttf", 8)

    bigColor = (128, 216, 255)
    smallColor = (128, 216, 255)
    glyphBgColor = (0, 145, 234)
    bgColor = (0, 176, 255)

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
                           (i * 20 + 18, j * 20 + 18)), fill=glyphBgColor)

    image.save("../Output/Scaffold.png")


if __name__ == "__main__":
    main()
