import streamlit as st

def calculate_total(price, num_people, bag_fee, platform_fee, discount):
    if num_people == 0:
        return 0
    item_price = price // num_people  # 均分產品價格
    total = max(0, item_price + bag_fee + platform_fee - discount)  # 計算總金額並確保不小於0
    return total

st.title('復胖達周二星巴克買一送一計算器')

st.header('拿鐵')
latte_price = st.number_input('請輸入拿鐵的價格', min_value=0, format='%d')
latte_people = st.number_input('要均分的人數（拿鐵）', min_value=1, format='%d')

st.header('美式')
americano_price = st.number_input('請輸入美式的價格', min_value=0, format='%d')
americano_people = st.number_input('要均分的人數（美式）', min_value=1, format='%d')

st.header('提袋/材料費')
bag_price = st.number_input('請輸入提袋/材料費的價格', min_value=0, format='%d')
bag_people = st.number_input('要均分的人數（提袋/材料費）', min_value=1, format='%d')
bag_each = bag_price // bag_people

st.header('平台費')
platform_fee = st.number_input('請輸入平台費的價格', min_value=0, format='%d')
platform_people = st.number_input('要均分的人數（平台費）', min_value=1, format='%d')
platform_each = platform_fee // platform_people

st.header('特殊折扣')
discount_price = st.number_input('請輸入特殊折扣的總金額', min_value=0, format='%d')
discount_people = st.number_input('特殊折扣要均分的人數', min_value=1, format='%d')
discount_each = discount_price // discount_people

if st.button('計算每人支付金額'):
    total_latte = calculate_total(latte_price, latte_people, bag_each, platform_each, discount_each)
    total_americano = calculate_total(americano_price, americano_people, bag_each, platform_each, discount_each)

    st.write(f'購買拿鐵，應支付明細：')
    st.write(f'- 拿鐵單價：${latte_price}，均分到 {latte_people} 人，每人：${latte_price // latte_people}')
    st.write(f'- 提袋/材料費：${bag_price}，均分到 {bag_people} 人，每人：${bag_each}')
    st.write(f'- 平台費：${platform_fee}，均分到 {platform_people} 人，每人：${platform_each}')
    st.write(f'- 特殊折扣：-${discount_price}，均分到 {discount_people} 人，每人：-${discount_each}')
    st.write(f'總支付金額（包含其他費用和折扣）：${total_latte} 元')

    st.write(f'購買美式，應支付明細：')
    st.write(f'- 美式單價：${americano_price}，均分到 {americano_people} 人，每人：${americano_price // americano_people}')
    st.write(f'- 提袋/材料費：${bag_price}，均分到 {bag_people} 人，每人：${bag_each}')
    st.write(f'- 平台費：${platform_fee}，均分到 {platform_people} 人，每人：${platform_each}')
    st.write(f'- 特殊折扣：-${discount_price}，均分到 {discount_people} 人，每人：-${discount_each}')
    st.write(f'總支付金額（包含其他費用和折扣）：${total_americano} 元')
