# Описания эндпоинтов
DESCRIPTIONS = {
    'SETTING_DEVICE': ('Подразумевается использование следующих приборов:\n'
                       '- Анализатор спектра: Signal Hound SM200B;\n'
                       '- Высокочастотный генератор: AnaPico RFSG6;\n'
                       '- Низкочастотный генератор: Agilent 33220A'),
}

DEFAULT_SET_INSTR = {
    'SIGNAL_GEN':{
        'REF_EXT': 10000000,
        'MODE': 'CW',
        'OUT_LVL': 25,
    }
}