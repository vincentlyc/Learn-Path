# fn_embed.py

def fn_outer():
	print("外部函數被調用")

	def fn_inner():
		print("fn_inner被調用")
	fn_inner()
	fn_inner()

	print("外部函數調用結束")

fn_outer()
# fn_inner()  # 錯的,內嵌函數只存在于函數內部