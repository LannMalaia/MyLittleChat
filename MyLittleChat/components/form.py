import reflex as rx
from MyLittleChat.systems.mlcState import State as st

good = {
    "없음": "우호적인 표상이 없습니다.",
    "라이너스": "라이너스와의 좋은 인연이 있습니다.",
    "3시대인": "3시대의 사람들과 좋은 인연이 있습니다.",
    "아드바리아교": "아드바리아교와 좋은 인연이 있습니다.",
    "오버라이터스": "오버라이터스와 좋은 인연이 있습니다.",
    "시청": "시청 공무원들과 좋은 인연이 있습니다.",
    "우상": "긍정적 의미로 사람들의 귀감이 되었습니다.",
    "마법학회": "마법학회와 좋은 인연이 있습니다.",
    "해적": "해적들과 좋은 인연이 있습니다.",
    "상인": "상단의 상인들과 좋은 인연이 있습니다.",
    "악마": "악마와 좋은 인연이 있습니다.",
    "세계수": "세계수와 좋은 인연이 있습니다."
}
bad = {
    "없음": "적대적인 표상이 없습니다.",
    "라이너스": "라이너스와 악연이 있습니다.",
    "3시대인": "3시대의 사람들과 악연이 있습니다.",
    "아드바리아교": "아드바리아교와 악연이 있습니다.",
    "오버라이터스": "오버라이터스와 악연이 있습니다.",
    "시청": "시청 공무원들과 악연이 있습니다.",
    "우상": "악명을 떨쳐 사람들의 표적이 되었습니다.",
    "마법학회": "마법학회와 악연이 있습니다.",
    "해적": "해적들과 악연이 있습니다.",
    "상인": "상단의 상인들과 악연이 있습니다.",
    "악마": "악마와 악연이 있습니다.",
    "세계수": "세계수와 악연이 있습니다."
}

class SymbolSelector(rx.ComponentState):
    symbol: str
    desc: str

    @rx.event
    def change_symbol_good(cls, value: str):
        cls.symbol = value
        cls.desc = good[value]
    @rx.event
    def change_symbol_bad(cls, value: str):
        cls.symbol = value
        cls.desc = bad[value]

    @classmethod
    def get_component(cls, is_good: bool, **props):
        name = "우호적인" if is_good else "적대적인"
        return rx.hstack(
            rx.text(f"{name} 표상"),
            rx.vstack(
                rx.hstack(
                    rx.select(
                        good.keys(),
                        value=cls.symbol,
                        on_change=cls.change_symbol_good if is_good else cls.change_symbol_bad,
                        default_value="없음",
                        width="130px"
                    ),
                    rx.text(
                        cls.desc
                    )
                ),
                long_textarea(placeholder=f"{name} 이유")
            )
        )

symbol_selector = SymbolSelector.create
def long_textarea(placeholder: str):
    return rx.text_area(
        placeholder=placeholder,
        style={
            "flex":"1",
            "overflow":"auto",
            "width":"100%"
        }
    )