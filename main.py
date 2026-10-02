from pyscript import display, document # type: ignore (searched it on Google)

def SKU_generator(e):
    
    category = document.getElementById('category').value
    product = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value
    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + str(stock_qty)
    display("SKU: ", sku, target='output')

def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    
    subtotal = (float(prod1.value) * prod1.checked +
            float(prod2.value) * prod2.checked +
            float(prod3.value) * prod3.checked +
            float(prod4.value) * prod4.checked +
            float(prod5.value) * prod5.checked)


    tax_rate = 0.12 
    vat = subtotal * tax_rate
    total = subtotal + vat 


    receipt = f"""==== Receipt ====
Subtotal: ₱{subtotal:.2f}
Tax: ₱{tax_rate:.2f}
Total: ₱{total:.2f}"""
    
    
    document.getElementById('show').innerText = receipt # (innerText adds breaks)
