laptop = 0
phone = 0
tablet = 0
running = True

while running:
    select = input("\n=== Menu ===" \
    "\n1. Xem báo cáo tồn kho" \
    "\n2. Nhập kho" \
    "\n3. Xuất kho" \
    "\n4. Cảnh báo hàng tồn kho thấp" \
    "\n5. Thoát chương trình" \
    "\nNhập lựa chọn của bạn: ")
    while True:
        try:
            select = int(select)
            if select <= 0 or select > 5:
                raise Exception()
            break
        except:
            select = input("Lựa chọn của bạn không hợp lệ, vui lòng nhập lại: ")
    
    match select:
        case 1:
            laptop_stars = ""
            for star in range(1, laptop + 1):
                laptop_stars = f"{laptop_stars}*"
            print(f"Laptop ({laptop}): {laptop_stars}")

            phone_stars = ""
            for star in range(1, phone + 1):
                phone_stars = f"{phone_stars}*"
            print(f"Phone ({phone}): {phone_stars}")

            tablet_stars = ""
            for star in range(1, tablet + 1):
                tablet_stars = f"{tablet_stars}*"
            print(f"Tablet ({tablet}): {tablet_stars}")
        case 2:
            item = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ")
            while True:
                try:
                    item = int(item)
                    if item <= 0 or item > 3:
                        raise Exception()
                    break
                except:
                    item = input("Không hợp lệ, nhập lại: ")
            
            quantity = input("Nhập số lượng cần thêm: ")
            while True:
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise Exception()
                    break
                except:
                    quantity = input("Số lượng không hợp lệ, vui lòng nhập lại! ")
            
            if item == 1:
                laptop += quantity
            else:
                if item == 2:
                    phone += quantity
                else:
                    tablet += quantity
        case 3:
            item = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ")
            while True:
                try:
                    item = int(item)
                    if item <= 0 or item > 3:
                        raise Exception()
                    break
                except:
                    item = input("Không hợp lệ, nhập lại: ")
            
            quantity = input("Nhập số lượng cần xuất: ")
            while True:
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise Exception()
                    break
                except:
                    quantity = input("Số lượng không hợp lệ, vui lòng nhập lại! ")
            
            if item == 1:
                if quantity > laptop:
                    print("Không đủ hàng")
                else:
                    laptop -= quantity
            else:
                if item == 2:
                    if quantity > phone:
                        print("Không đủ hàng")
                    else:
                        phone -= quantity
                else:
                    if quantity > tablet:
                        print("Không đủ hàng")
                    else:
                        tablet -= quantity
        case 4:
            if laptop < 10:
                print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")
            if phone < 10:
                print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {phone} sản phẩm)")
            if tablet < 10:
                print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")
        case 5:
            print("Đã thoát chương trình")
            running = False
            break