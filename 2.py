# phan tich loi
    # express_orders de  "GE100-FAST" thanh index thu nhat
    # vi khi day o insert thi "GE102-WRONG" tu 1 thanh 2
    # express_orders[1] = "GE102-UPDATED" đã ghi đè vào vị trí index 1 nen bi sai don
    # vi khi bi insert nhet vao thi so index da bi thay doi
    # express_orders.remove("GE103-CANCEL")
    # pop() khong co index se xoa phan tu cuoi
# sua loi
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102-UPDATED"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)
print(f"Danh sách đơn hàng còn lại: {express_orders}")
print(f"Đơn hàng đang giao: {current_order}")