from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform

_io = [
    ("ps_clk", 0, Pins("E7"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("ps_srstb", 0, Pins("B10"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("ps_porb", 0, Pins("C7"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    # Green and Red LEDs
    ("user_led", 0, Pins("W13"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("W14"), IOStandard("LVCMOS33")),
    # Push Buttons
    ("user_btn", 0, Pins("A17"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("A14"), IOStandard("LVCMOS33")),
    # UART
    (
        "serial",
        0,
        Subsignal("tx", Pins("A16")),
        Subsignal("rx", Pins("F15")),
        IOStandard("LVCMOS33"),
    ),
    # JTAG
    (
        "jtag",
        Subsignal("tms", Pins("J6")),
        Subsignal("tdo", Pins("F6")),
        Subsignal("tdi", Pins("G6")),
        Subsignal("tck", Pins("F9")),
        IOStandard("LVCMOS33"),
    ),
    # DDR3
    (
        "ddram",
        0,
        Subsignal(
            "a",
            Pins("N2 K2 M3 K3 M4 L1 L4 K4 K1 J4 F5 G4 E4 D4 F4"),
            IOStandard("SSTL15"),
        ),
        Subsignal("ba", Pins("L5 R4 J5"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("P4"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("P5"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("M5"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("N1"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("A1 F1"), IOStandard("SSTL15_T_DCI")),
        Subsignal(
            "dq",
            Pins("C3 B3 A2 A4 D3 D1 C1 E1 E2 E3 G3 H3 J3 H2 H1 J1"),
            IOStandard("SSTL15_T_DCI"),
        ),
        Subsignal(
            "dqs_p",
            Pins("C2 G2"),
            IOStandard("DIFF_SSTL15_T_DCI"),
        ),
        Subsignal(
            "dqs_n",
            Pins("B2 F2"),
            IOStandard("DIFF_SSTL15_T_DCI"),
        ),
        Subsignal("clk_p", Pins("L2"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("M2"), IOStandard("DIFF_SSTL15")),
        Subsignal("cke", Pins("N3"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("N5"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("B4"), IOStandard("SSTL15")),
        Misc("SLEW=FAST"),
    ),
    # NAND Flash
    (
        "nandflash",
        0,
        Subsignal("nand_data", Pins("A6 A5 B7 E8 B5 E9 C6 D9")),
        Subsignal("nand_ce", Pins("E6")),
        Subsignal("nand_re", Pins("D5")),
        Subsignal("nand_we", Pins("D6")),
        Subsignal("nand_ale", Pins("B8")),
        Subsignal("nand_cle", Pins("D8")),
        Subsignal("nand_rb", Pins("C5")),
        IOStandard("LVCMOS33"),
    ),
    # ETH PHY
    (
        "eth_clocks",
        0,
        Subsignal("rxclk", Pins("U14")),
        Subsignal("txclk", Pins("U15")),
        IOStandard("LVCMOS33"),
    ),
    (
        "eth",
        0,
        Subsignal("rx_dv", Pins("W16")),
        Subsignal("rx_data", Pins("Y16 V16 V17 Y17")),
        Subsignal("tx_en", Pins("W19")),
        Subsignal("tx_data", Pins("W18 Y18 V18 Y19")),
        Subsignal("mdc", Pins("W15")),
        Subsignal("mdio", Pins("Y14")),
        IOStandard("LVCMOS33"),
    ),
    # SD Card
    (
        "sdcard",
        0,
        Subsignal("detect", Pins("A12"), Misc("PULLUP True")),
        Subsignal("data", Pins("E12 A9 F13 B15")),
        Subsignal("cmd", Pins("C17")),
        Subsignal("clk", Pins("D14")),
        Subsignal("cd", Pins("B15")),
        IOStandard("LVCMOS33"),
        Misc("SLEW=FAST"),
    ),
]

# DATA1-3 2x10 2.0mm Pitch
# J3 and J5 1x4 2.54mm Pitch (opto-isolators if populated)
_connectors = [
    (
        "DATA1",
        {
            "DATA1-5": "A20",
            "DATA1-6": "H16",
            "DATA1-7": "B19",
            "DATA1-8": "B20",
            "DATA1-9": "C20",
            "DATA1-11": "H17",
            "DATA1-13": "D20",
            "DATA1-14": "D18",
            "DATA1-15": "H18",
            "DATA1-16": "D19",
            "DATA1-17": "F20",
            "DATA1-18": "E19",
            "DATA1-19": "F19",
            "DATA1-20": "K17",
        },
    ),
    (
        "DATA2",
        {
            "DATA2-5": "G20",
            "DATA2-6": "J18",
            "DATA2-7": "G19",
            "DATA2-8": "H20",
            "DATA2-9": "J19",
            "DATA2-11": "K18",
            "DATA2-13": "K19",
            "DATA2-14": "J20",
            "DATA2-15": "L16",
            "DATA2-16": "L19",
            "DATA2-17": "M18",
            "DATA2-18": "L20",
            "DATA2-19": "M20",
            "DATA2-20": "L17",
        },
    ),
    (
        "DATA3",
        {
            "DATA3-5": "M19",
            "DATA3-6": "N20",
            "DATA3-7": "P18",
            "DATA3-8": "M17",
            "DATA3-9": "N17",
            "DATA3-11": "P20",
            "DATA3-13": "R18",
            "DATA3-14": "R19",
            "DATA3-15": "P19",
            "DATA3-16": "T20",
            "DATA3-17": "U20",
            "DATA3-18": "T19",
            "DATA3-19": "V20",
            "DATA3-20": "U19",
        },
    ),
    (
        "J3",
        {
            "J3-4-TX": "U12",
            "J3-3-RX": "V13",
        },
        "J5",
        {
            "J5-4-TX": "V12",
            "J5-3-RX": "V15",
        },
    ),
]


class EBAZ4205Platform(XilinxPlatform):
    default_clk_name = "ps_clk"
    default_clk_period = 1e9 / 33.333e6  # 33.333 MHz

    def __init__(self):
        XilinxPlatform.__init__(
            self, "xc7z010-clg400-1", _io, _connectors, toolchain="vivado"
        )
