while True:
    mohasebe = int(input("Masahat: 1.moraba 2.mostatil 3.dayere 4.mosalas 5.lozi 6.motavaziol.azla 7.zozanaghe 8.ostovane 9.kore 10.heram\nMohit: 11.moraba 12.mostatil 13.dayere 14.mosalas 15.lozi 16.motavazol.azla 17.zozanaghe 18.ostovane 19.kore 20.heram\n21.tavan 22.fucktorial 23.fibonachi 24.mohasebe takhfif 25.print jadval zarb1,10 26.hal ebarat riazi\n100.moshakhasat barname 0.Exit: "))
    if mohasebe == 0:
        print("Exit")
        break
    match mohasebe:
        case 1:
            MM1 = float(input("Tool moraba ra vared konid: "))
            print(MM1 * MM1)
        case 2:
            MO1 = float(input("Tool mostatil ra vared konid: "))
            MO10 = float(input("Arz mostatil ra vared konid: "))
            print(MO1 * MO10)
        case 3:
            MD1 = float(input("Shoaye dayere ra vared konid: "))
            print(MD1 * MD1 * 3.14)
        case 4:
            MS1 = float(input("ghaede ye mosalas ra vared konid: "))
            MS10 = float(input("ertefa ye mosalas ra vared konid: "))
            print(MS1 * MS10 / 2)
        case 5:
            ML1 = float(input("Ghotr bozorg lozi ra vared konid: "))
            ML10 = float(input("Ghotr kochak lozi ra vared konid: "))
            print(ML1 * ML10 / 2)
        case 6:
            MZ1 = float(input("Ghaede motavaziol.azla ra vared konid: "))
            MZ10 = float(input("Ertefa motavaziol.azla ra vared konid: "))
            print(MZ1*MZ10)
        case 7:
            MN1 = float(input("Ghaede aval zozanaghe ra vared konid: "))
            MN10 = float(input("Ghaede dovom zozanaghe ra vared konid: "))
            MN100 = float(input("Ertefa zozanaghe ra vared konid: "))
            print((MN1 + MN10)*MN100/2)
        case 8:
            ME1 = float(input("Shoae ghaede ostovane ra vared konid: "))
            ME10 = float(input("Ertefa ostovane ra vared konid: "))
            masahat_janebi = 2 * 3.14 * ME1 * ME10
            masahat_ghaede = 3.14 * (ME1 ** 2)
            print(masahat_janebi + 2 * masahat_ghaede)
        case 9:
            MK1 = float(input("Shoae kore ra vared konid: "))
            print(4 * 3.14 * (MK1 ** 2))
        case 10:
            MH1 = float(input("Tool zel ghaede moraba heram ra vared konid: "))
            MH10 = float(input("Masahat janebi heram ra vared konid (sum of areas of triangular faces): "))
            masahat_ghaede_heram = MH1 ** 2
            print(masahat_ghaede_heram + MH10)
        case 11:
            TM1 = float(input("Tool moraba ra vared konid: "))
            print(TM1 * 4)
        case 12:
            TO1 = float(input("Tool mostatil ra vared konid: "))
            TO10 = float(input("Arz mostatil ra vared konid: "))
            print(TO1 + TO10 + TO1 + TO10)
        case 13:
            TD1 = float(input("Shoaye dayere ra vared konid: "))
            print(TD1 * 3.14 * 2)
        case 14:
            TS1 = float(input("Zel 1 ra vared konid: "))
            TS10 = float(input("Zel 2 ra vared konid: "))
            TS11 = float(input("Zel 3 ra vared konid: "))
            print(TS1 + TS10 + TS11)
        case 15:
            TL1 = float(input("Tool lozi ra vared konid: "))
            print(TL1 * 4)
        case 16:
            MZ1o = float(input("Tool yek zele motavaziol.azla ra vared konid: "))
            MZ10o = float(input("Tool zele mojaveR motavaziol.azla ra vared konid: "))
            print(2 * (MZ1o + MZ10o))
        case 17:
            MN1o = float(input("Tool zele aval zozanaghe ra vared konid: "))
            MN10o = float(input("Tool zele dovom zozanaghe ra vared konid: "))
            MN100o = float(input("Tool zele sevom zozanaghe ra vared konid: "))
            MN1000o = float(input("Tool zele chaharum zozanaghe ra vared konid: "))
            print(MN1o + MN10o + MN100o + MN1000o)
        case 18:
            ME1o = float(input("Shoaye ghaedeh ostovane ra vared konid: "))
            print(2 * 3.14 * ME1o)
        case 19:
            MK1o = float(input("Shoaye kore ra vared konid: "))
            print(2 * 3.14 * MK1o)
        case 20:
            MH1o = float(input("Tool zel ghaede moraba heram ra vared konid: "))
            print(4 * MH1o)
        case 21:
            T0 = float(input("Adadi ke mikhahid be tavan ? beresad ra vared konid: "))
            T1 = float(input("Tavan ada ra vared konid: "))
            print(T0 ** T1)
        case 22:
            numf = int(input("Adadi ke mikhjid fuktorualash ra hesab konid ra vared konid: "))
            resf = 1
            for i in range(1, numf + 1):
                resf*=i
            print(f"======={numf}========")
        case 23:
            n = int(input("Adadi ke mikhahid fibonachi ash ra be dast avarid ra vared konid: "))
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
                print(a)
        case 24:
            gheymat = float(input("gheymat ra vared konid: "))
            takhfif = float(input("takhfif ra vared konid: "))
            baghi_mande = 100 - takhfif
            gheymat_nahayi = baghi_mande / 100 * gheymat
            print("=====================================")
            print("---------gheymat nahayi{}---------".format(gheymat_nahayi))
            print("=====================================")
        case 25:
            for i in range(1, 11):
                print(f"jadval zarb 1,10 {i}:")
                for j in range(1, 11):
                    hasel_zarb = i * j
                    print(f"{i} * {j:2} = {hasel_zarb:3}")
                print("-" * 20)
        case 26:
            AR = input("EBARAT RIAZI KHOD RA VARED KONID: ")
            result = eval(AR)
            print(f"RESULT = {result}")
        case 100:
            print("========================================================================")
            print("1,10:be dast avordan masahat 10 shekl hendesi motafavet.")
            print("11,20:be dast avordan mohit 10 shekl hendesi motafavet.")
            print("21,25:tavan,fucktorial,fibonachi,mohasebe takhfif,print jadval zarb1,10,hal ebarat riazi")
            print("dar hal erafiki shodan")
            print("zaban barname:python")
            print("barname nevis:Shayan-FM")
            print("========================================================================")
        case _:
            print("IN GOZINE VOJOD NADARAD!")
            
