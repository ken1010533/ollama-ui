  

def 視窗至中(窗口):



    螢幕寬=窗口.winfo_screenwidth()    # 取得螢幕寬度
    螢幕高=窗口.winfo_screenheight()  # 取得螢幕高度

    視窗寬 = int((螢幕寬)/3)
    視窗高 = int((螢幕高)/3)

    左上x軸=int((螢幕寬-視窗寬)/2)       # 計算左上 x 座標
    左上y軸=int((螢幕高-視窗高)/2)      # 計算左上 y 座標
    窗口.geometry(f'{視窗寬}x{視窗高}+{左上x軸}+{左上y軸}')     #要將視窗置中顯示