import reflex as rx
from MyLittleChat.systems.mlcState import State as st

symbol_desc = {
    "없음": "흔히 마주치는 사람들 중의 하나였습니다. 어디선가 활약한 경험도, 우연한 기회도, 특별한 인연도 없었습니다. 도시에 처음 온 이방인일수도 있습니다.",
    "라이너스": "라이너스는 세계적인 모험가 길드입니다. 라이너스는 도시마다 지부를 두고 있으며, 도시 사람들의 각종 심부름을 해결해주지만, 보통의 경우 시청이나 국가로부터 몬스터 토벌 의뢰를 받아 짧은 모험을 떠나고는 합니다.",
    "3시대인": "3시대인들은 우주로 나아간 이전 시대의 사람들입니다. 비행선을 몰며 우주를 여행하는 그들은 현재의 우리들보다도 더 미래적인 발전을 이룬 집단이지만, 발전과 맞바꾼 번식능력으로 인해 인구 수가 적습니다. 그들은 세계수가 위치한 세계를 관찰하는 것에 흥미가 있으며, 종종 사람들을 납치해 실험에 쓰고는 하는 무서운 면모도 가지고 있습니다.",
    "아드바리아교": "아드바리아교단은 영광의 여신 아드바리아를 모시는 자들의 집단입니다. 현재의 기독교와 비슷한 위치, 비슷한 교리를 지니고 있으며, 옳고 그름보다는 영광스러운 행동을 중시하기 때문에 때때로 문제를 일으키기도 합니다. 그들 중 일부는 아드바리아 여신의 선택을 받고, 그녀의 의뢰를 해내는 임무를 수행하기도 합니다.",
    "오버라이터스": "오버라이터스는 시간을 다루는 것을 목적으로 하는 비밀 조직입니다. 이들은 매우 비밀스럽고도 암암리에서만 활동하는 조직이기 때문에, 만나는 것조차도 쉽지 않습니다. 오버라이터스는 시간을 조작하려는 목적으로 인해, 국가에서는 테러리스트 단체로 지명되어 있습니다. 즉, 일원이 되는 순간 범죄자가 되는 겁니다. 그들은 일원 하나하나가 정예로 이루어져 있기에, 상대하기가 쉽지 않습니다.",
    "시청": "시청은 말 그대로 도시의 시청을 뜻합니다. 그들은 무엇보다도 규칙과 규율을 중시하며, 도시의 안전을 최우선으로 하는 단체입니다. 공무원이나 명예시민, 시의원 정도의 입지를 가졌다면 시청과도 좋은 인연이 있다고 할 수 있습니다.",
    "우상": "우상은 인기가 많은 사람을 나타냅니다. 춤과 노래에 능하거나, 외모가 아름답다거나, 인품이 훌륭하다거나, 혹은 악명을 떨쳤거나 안 좋은 의미의 인기를 얻었을 수도 있습니다. 우상이 된 사람을 모르는 사람들은 거의 없습니다.",
    "마법학회": "마법학회는 마법을 다루는 사람들의 학술적 연구회 같은 곳입니다. 고차원의 마법은 부릴 수 없는 세계이기에 그런 것을 배우는 학생들은 많지 않지만, 이론상 가능한 것들을 연구하고자 하는 이들은 어디에나 있기 마련입니다. 그들은 마나를 잘 다룰 줄 알며, 마법 무용론자들에게는 적개심을 가집니다.",
    "해적": "해적단 황게이는 동쪽 대륙에서 건너 온 초대규모 해적단입니다. 그들은 작은 나라 하나를 점령할 만큼의 해상 전투력을 보유한 단체로, 바다에서는 그들을 상대할만한 단체가 별로 없습니다. 육지에서는 동쪽 대륙에서 가져온 알지 못할 함정, 몬스터, 독극물 따위로 사람들을 골치 아프게 하는 집단이며, 개인의 강함과는 별개로 물량으로 밀어붙이는 스타일입니다.",
    "상인": "상단은 도시와 도시를 오고 가는 단체입니다. 여러 상단이 있으며, 도시에 오는 상단의 수도 다양합니다. 그들은 막대한 재력을 가지고 있으며, 그것으로 사람을 고용해 자기들 대신에 움직이게 하는 것이 곧 그들의 힘이 됩니다. 상단은 달마다 오는 상단도 있지만, 대개 두 세 달 단위로 도시 사이를 돌아다닙니다.",
    "악마": "악마는 완전히 구별된 세계인 마계에 살고 있는 자들입니다. 그들은 저마다의 욕망과 야욕에 의해서만 움직이며, 형태가 없어 아무 모습으로나 변할 수 있는 자들입니다. 몇몇은 인간들에게 큰 관심이 있어, 인간들과 계약을 하고 그들의 세계에 넘어오려고 하기도 합니다.",
    "세계수": "세계수는 마법을 구성하는 에너지인 마나를 생산해내는 거대한 나무의 군집체입니다. 사람이나 집단이 아니기에 세계수 자체와의 인연은 없으나, 그것이 만들어낸 정령이나 마법 아이템으로 인해 세계수와의 인연이 탄생합니다. 세계수와 인연이 있는 자들은 신성하거나 존엄한 위치의 사람들에게 인정을 받습니다."
}
symbol_good = {
    "없음": "우호적인 표상이 없습니다. 캐릭터를 도와줄 사람이 없네요.",
    "라이너스": "라이너스 길드와의 좋은 인연이 있습니다. 길드원들을 도와줬거나, 혹은 캐릭터가 길드의 일원일 수 있습니다.",
    "3시대인": "3시대의 사람들과 좋은 인연이 있습니다. 3시대인들 중 하나거나, 그들의 친구일수도 있습니다.",
    "아드바리아교": "아드바리아교와 좋은 인연이 있습니다. 교인이거나, 그들을 도왔거나, 아드바리아 여신의 선택을 받았을 수 있습니다.",
    "오버라이터스": "오버라이터스와 좋은 인연이 있습니다. 비밀스러운 집단의 일원이 되기란 어렵습니다.",
    "시청": "시청 공무원들과 좋은 인연이 있습니다.",
    "우상": "긍정적 의미로 사람들의 귀감이 되었습니다.",
    "마법학회": "마법학회와 좋은 인연이 있습니다.",
    "해적": "해적들과 좋은 인연이 있습니다.",
    "상인": "상단의 상인들과 좋은 인연이 있습니다.",
    "악마": "악마와 좋은 인연이 있습니다.",
    "세계수": "세계수와 좋은 인연이 있습니다."
}
symbol_bad = {
    "없음": "적대적인 표상이 없습니다. 그래도 나쁜 짓은 안한 것 같습니다.",
    "라이너스": "라이너스와 악연이 있습니다. 중요한 임무 중에 도망쳤거나, 다른 길드원을 배신했거나, 길드나 길드원에게 해를 끼쳤을 가능성이 높습니다.",
    "3시대인": "3시대의 사람들과 악연이 있습니다. 캐릭터가 실험에 이용됐다거나, 실험 대상으로 지목되어 쫓기게 되었다거나, 다른 3시대인을 다치게 했을 수 있습니다.",
    "아드바리아교": "아드바리아교와 악연이 있습니다. 교리를 어겼거나 교단원에게 피해를 입히는 등 교단에 피해를 끼쳤을 수 있습니다. 여신에게 수배당한 상태일수도 있습니다.",
    "오버라이터스": "오버라이터스와 악연이 있습니다. 그들과 적대적인 관계가 되는 것은 그렇게 좋은 생각은 아닙니다. 캐릭터는 오버라이터스의 정체를 캐고 있거나, 일망타진할 계획을 짜고 있을 수 있습니다.",
    "시청": "시청 공무원들과 악연이 있습니다. 지명수배자거나, 세금이 체납됐거나, 범법을 저질렀을 가능성이 있습니다. 혹은 정치적인 이유 등으로 시청 공무원들이 아무 이유없이 캐릭터를 노리고 있을수도 있습니다.",
    "우상": "악명을 떨쳐 사람들의 표적이 되었습니다.",
    "마법학회": "마법학회와 악연이 있습니다. 캐릭터가 마나리스거나, 마법 무용론자거나, 학회에 피해를 끼쳤거나, 그냥 마법을 너무 못 다루는 사람일수도 있습니다.",
    "해적": "해적들과 악연이 있습니다. 해적들은 대부분을 적으로 두고 있습니다. 단지 돈이 많거나, 명예로운 직위에 있기만 해도 그들의 타겟이 됩니다.",
    "상인": "상단의 상인들과 악연이 있습니다. 사기를 쳤거나, 습격을 하는 등 곤란한 상황에 처하게 했을 수 있습니다. 상단은 용병을 고용하거나, 친한 이들을 이용해 당신을 곤란하게 합니다.",
    "악마": "악마와 악연이 있습니다. 악마를 속이거나, 악마에게 배척받는 존재일 수 있습니다. 악마들은 몬스터를 폭주시키고, 다른 캐릭터에 빙의하는 식으로 적대적 성향을 드러냅니다.",
    "세계수": "세계수와 악연이 있습니다. 이전 시대의 사람들의 후손이거나, 캐릭터가 몬스터거나, 세계수를 해할 운명을 가졌을 수 있습니다. 신성한 존재들이 적대적 성향을 드러냅니다."
}

class SymbolSelector(rx.ComponentState):
    symbol: str
    desc: str
    good_bad: str

    @rx.event
    def change_symbol_good(cls, value: str):
        cls.symbol = value
        cls.desc = symbol_desc[value]
        cls.good_bad = symbol_good[value]
    @rx.event
    def change_symbol_bad(cls, value: str):
        cls.symbol = value
        cls.desc = symbol_desc[value]
        cls.good_bad = symbol_bad[value]

    @classmethod
    def get_component(cls, is_good: bool, **props):
        name = "우호적인" if is_good else "적대적인"
        return rx.hstack(
            rx.text(f"{name} 표상"),
            rx.vstack(
                rx.select(
                    symbol_good.keys(),
                    value=cls.symbol,
                    on_change=cls.change_symbol_good if is_good else cls.change_symbol_bad,
                    default_value="없음",
                    width="130px"
                ),
                rx.text(
                    cls.desc
                ),
                rx.text(
                    cls.good_bad
                ),
                rx.cond(
                    cls.symbol != "없음",
                    long_textarea(placeholder=f"표상과 {name} 이유"),
                ),
                style={
                    "flex":"1",
                    "width":"100%"
                }
            ),
            style={
                "flex":"1",
                "width":"100%"
            }
        )

symbol_selector = SymbolSelector.create

def long_textarea(placeholder: str) -> rx.Component:
    return rx.text_area(
        placeholder=placeholder,
        size="3",
        variant="surface",
        radius="large",
        style={
            "flex":"1",
            "overflow":"auto",
            "width":"100%"
        }
    )
def short_textline(placeholder: str) -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        size="3",
        variant="surface",
        radius="large",
        max_length=20,
        min_length=3,
        style={
            "width":"15em",
            "padding":"0.5em 0"
        }
    )
def long_textline(placeholder: str) -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        size="3",
        variant="surface",
        radius="large",
        max_length=40,
        min_length=3,
        style={
            "flex":"1",
            "overflow":"auto",
            "width":"100%",
            "padding":"0.5em 0"
        }
    )
def aspect_input(placeholder: str) -> rx.Component:
    return rx.flex(
        long_textline(placeholder=placeholder),
        rx.icon_button("minus", size="3"),
        spacing="2",
        style={
            "flex":"1",
            "width":"100%"
        }
    )
def skill_input() -> rx.Component:
    return rx.flex(
        short_textline(placeholder="특기명"),
        long_textline(placeholder="특기 설명"),
        spacing="2",
        style={
            "flex":"1",
            "width":"100%"
        }
    )

stat_badge_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}
class StatSelector(rx.ComponentState):

    stats: list[list[str]] = [
        ["기술", "마법학", "학식", "범죄", "사교", "속임수", 
        "자극", "주의력", "운전", "운동능력", "체력", "의지력", "접근전", "사격"],
        [],
        [],
        [],
        []  # 각 레벨의 선택 상태
    ]

    @rx.event
    def up_stat(cls, value: str):
        for i in range(5):
            arr = cls.stats[i]
            if value in arr:
                if i < 4:
                    up_arr = cls.stats[i + 1]
                    if len(up_arr) < len(arr) - 1:
                        arr.remove(value)
                        cls.stats[i + 1].append(value)
                    else:
                        return rx.toast("피라미드 구조에 위배됩니다.")
                    return
                else:
                    return rx.toast("범위를 벗어났습니다.")
    @rx.event
    def down_stat(cls, value: str):
        for i in range(5):
            arr = cls.stats[i]
            if value in arr:
                if i > 0:
                    arr.remove(value)
                    cls.stats[i - 1].append(value)
                    return
                else:
                    return rx.toast("범위를 벗어났습니다.")

    @classmethod
    def get_component(cls, **props):
        def selected_item_chip(item: str) -> rx.Component:
            return rx.badge(
                rx.icon("arrow_up", size=18, on_click=cls.up_stat(item)),
                item,
                rx.icon("arrow_down", size=18, on_click=cls.down_stat(item)),
                color_scheme="green",
                **stat_badge_props,
                # on_click=cls.up_stat(item)
            )
        
        return rx.vstack(
            rx.hstack(
                rx.text("+4 (대단함)", align="center", style={"width":"7em"}),
                rx.divider(orientation="vertical"),
                rx.flex(
                    rx.foreach(
                        cls.stats[4], selected_item_chip
                    ),
                    spacing="2",
                    flex_wrap="wrap",
                    style={
                        "flex":"1",
                        "width":"100%"
                    }
                )
            ),
            rx.hstack(
                rx.text("+3 (우수함)", align="center", style={"width":"7em"}),
                rx.divider(orientation="vertical"),
                rx.flex(
                    rx.foreach(
                        cls.stats[3], selected_item_chip
                    ),
                    spacing="2",
                    flex_wrap="wrap",
                    style={
                        "flex":"1",
                        "width":"100%"
                    }
                )
            ),
            rx.hstack(
                rx.text("+2 (양호함)", align="center", style={"width":"7em"}),
                rx.divider(orientation="vertical"),
                rx.flex(
                    rx.foreach(
                        cls.stats[2], selected_item_chip
                    ),
                    spacing="2",
                    flex_wrap="wrap",
                    style={
                        "flex":"1",
                        "width":"100%"
                    }
                )
            ),
            rx.hstack(
                rx.text("+1 (평범함)", align="center", style={"width":"7em"}),
                rx.divider(orientation="vertical"),
                rx.flex(
                    rx.foreach(
                        cls.stats[1], selected_item_chip
                    ),
                    spacing="2",
                    flex_wrap="wrap",
                    style={
                        "flex":"1",
                        "width":"100%"
                    }
                )
            ),
            rx.hstack(
                rx.text("+0 (미약함)", align="center", style={"width":"7em"}),
                rx.divider(orientation="vertical"),
                rx.flex(
                    rx.foreach(
                        cls.stats[0], selected_item_chip
                    ),
                    spacing="2",
                    flex_wrap="wrap",
                    style={
                        "flex":"1",
                        "width":"100%"
                    }
                )
            )
        )
    
stat_selector = StatSelector.create