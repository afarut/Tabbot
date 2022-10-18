from keyboards import reply


async def splitter(message, text):
	lst = list(map(str, text.split("\n")))
	text = ""
	j = 0
	for i in lst:
		if len(text + i + '\n') > 4000:
			await asyncio.sleep(0.5)
			await message.answer(text, reply_markup=reply.menu())
			text = i + '\n'
		else:
			text += i + '\n'
		if j == 2:
			pass
		j += 1
	else:
		await message.answer(text, reply_markup=reply.menu())