
import profile
from speech import LangChangeCommand
import languageHandler
import config

# generated from _compile_scripts_txt

scriptCode= [
	( 0x0 , 0x1f , 998 ), # Common
	( 0x20 , 0x20 , 998 ), # Common
	( 0x21 , 0x23 , 998 ), # Common
	( 0x24 , 0x24 , 998 ), # Common
	( 0x25 , 0x27 , 998 ), # Common
	( 0x28 , 0x28 , 998 ), # Common
	( 0x29 , 0x29 , 998 ), # Common
	( 0x2a , 0x2a , 998 ), # Common
	( 0x2b , 0x2b , 998 ), # Common
	( 0x2c , 0x2c , 998 ), # Common
	( 0x2d , 0x2d , 998 ), # Common
	( 0x2e , 0x2f , 998 ), # Common
	( 0x30 , 0x39 , 998 ), # Common
	( 0x3a , 0x3b , 998 ), # Common
	( 0x3c , 0x3e , 998 ), # Common
	( 0x3f , 0x40 , 998 ), # Common
	( 0x41 , 0x5a , 215 ), # Latin
	( 0x5b , 0x5b , 998 ), # Common
	( 0x5c , 0x5c , 998 ), # Common
	( 0x5d , 0x5d , 998 ), # Common
	( 0x5e , 0x5e , 998 ), # Common
	( 0x5f , 0x5f , 998 ), # Common
	( 0x60 , 0x60 , 998 ), # Common
	( 0x61 , 0x7a , 215 ), # Latin
	( 0x7b , 0x7b , 998 ), # Common
	( 0x7c , 0x7c , 998 ), # Common
	( 0x7d , 0x7d , 998 ), # Common
	( 0x7e , 0x7e , 998 ), # Common
	( 0x7f , 0x9f , 998 ), # Common
	( 0xa0 , 0xa0 , 998 ), # Common
	( 0xa1 , 0xa1 , 998 ), # Common
	( 0xa2 , 0xa5 , 998 ), # Common
	( 0xa6 , 0xa6 , 998 ), # Common
	( 0xa7 , 0xa7 , 998 ), # Common
	( 0xa8 , 0xa8 , 998 ), # Common
	( 0xa9 , 0xa9 , 998 ), # Common
	( 0xaa , 0xaa , 215 ), # Latin
	( 0xab , 0xab , 998 ), # Common
	( 0xac , 0xac , 998 ), # Common
	( 0xad , 0xad , 998 ), # Common
	( 0xae , 0xae , 998 ), # Common
	( 0xaf , 0xaf , 998 ), # Common
	( 0xb0 , 0xb0 , 998 ), # Common
	( 0xb1 , 0xb1 , 998 ), # Common
	( 0xb2 , 0xb3 , 998 ), # Common
	( 0xb4 , 0xb4 , 998 ), # Common
	( 0xb5 , 0xb5 , 998 ), # Common
	( 0xb6 , 0xb7 , 998 ), # Common
	( 0xb8 , 0xb8 , 998 ), # Common
	( 0xb9 , 0xb9 , 998 ), # Common
	( 0xba , 0xba , 215 ), # Latin
	( 0xbb , 0xbb , 998 ), # Common
	( 0xbc , 0xbe , 998 ), # Common
	( 0xbf , 0xbf , 998 ), # Common
	( 0xc0 , 0xd6 , 215 ), # Latin
	( 0xd7 , 0xd7 , 998 ), # Common
	( 0xd8 , 0xf6 , 215 ), # Latin
	( 0xf7 , 0xf7 , 998 ), # Common
	( 0xf8 , 0x1ba , 215 ), # Latin
	( 0x1bb , 0x1bb , 215 ), # Latin
	( 0x1bc , 0x1bf , 215 ), # Latin
	( 0x1c0 , 0x1c3 , 215 ), # Latin
	( 0x1c4 , 0x293 , 215 ), # Latin
	( 0x294 , 0x294 , 215 ), # Latin
	( 0x295 , 0x2af , 215 ), # Latin
	( 0x2b0 , 0x2b8 , 215 ), # Latin
	( 0x2b9 , 0x2c1 , 998 ), # Common
	( 0x2c2 , 0x2c5 , 998 ), # Common
	( 0x2c6 , 0x2d1 , 998 ), # Common
	( 0x2d2 , 0x2df , 998 ), # Common
	( 0x2e0 , 0x2e4 , 215 ), # Latin
	( 0x2e5 , 0x2e9 , 998 ), # Common
	( 0x2ea , 0x2eb , 285 ), # Bopomofo
	( 0x2ec , 0x2ec , 998 ), # Common
	( 0x2ed , 0x2ed , 998 ), # Common
	( 0x2ee , 0x2ee , 998 ), # Common
	( 0x2ef , 0x2ff , 998 ), # Common
	( 0x300 , 0x36f , 994 ), # Inherited
	( 0x370 , 0x373 , 200 ), # Greek
	( 0x374 , 0x374 , 998 ), # Common
	( 0x375 , 0x375 , 200 ), # Greek
	( 0x376 , 0x377 , 200 ), # Greek
	( 0x37a , 0x37a , 200 ), # Greek
	( 0x37b , 0x37d , 200 ), # Greek
	( 0x37e , 0x37e , 998 ), # Common
	( 0x37f , 0x37f , 200 ), # Greek
	( 0x384 , 0x384 , 200 ), # Greek
	( 0x385 , 0x385 , 998 ), # Common
	( 0x386 , 0x386 , 200 ), # Greek
	( 0x387 , 0x387 , 998 ), # Common
	( 0x388 , 0x38a , 200 ), # Greek
	( 0x38c , 0x38c , 200 ), # Greek
	( 0x38e , 0x3a1 , 200 ), # Greek
	( 0x3a3 , 0x3e1 , 200 ), # Greek
	( 0x3e2 , 0x3ef , 204 ), # Coptic
	( 0x3f0 , 0x3f5 , 200 ), # Greek
	( 0x3f6 , 0x3f6 , 200 ), # Greek
	( 0x3f7 , 0x3ff , 200 ), # Greek
	( 0x400 , 0x481 , 220 ), # Cyrillic
	( 0x482 , 0x482 , 220 ), # Cyrillic
	( 0x483 , 0x484 , 220 ), # Cyrillic
	( 0x485 , 0x486 , 994 ), # Inherited
	( 0x487 , 0x487 , 220 ), # Cyrillic
	( 0x488 , 0x489 , 220 ), # Cyrillic
	( 0x48a , 0x52f , 220 ), # Cyrillic
	( 0x531 , 0x556 , 230 ), # Armenian
	( 0x559 , 0x559 , 230 ), # Armenian
	( 0x55a , 0x55f , 230 ), # Armenian
	( 0x561 , 0x587 , 230 ), # Armenian
	( 0x589 , 0x589 , 998 ), # Common
	( 0x58a , 0x58a , 230 ), # Armenian
	( 0x58d , 0x58e , 230 ), # Armenian
	( 0x58f , 0x58f , 230 ), # Armenian
	( 0x591 , 0x5bd , 125 ), # Hebrew
	( 0x5be , 0x5be , 125 ), # Hebrew
	( 0x5bf , 0x5bf , 125 ), # Hebrew
	( 0x5c0 , 0x5c0 , 125 ), # Hebrew
	( 0x5c1 , 0x5c2 , 125 ), # Hebrew
	( 0x5c3 , 0x5c3 , 125 ), # Hebrew
	( 0x5c4 , 0x5c5 , 125 ), # Hebrew
	( 0x5c6 , 0x5c6 , 125 ), # Hebrew
	( 0x5c7 , 0x5c7 , 125 ), # Hebrew
	( 0x5d0 , 0x5ea , 125 ), # Hebrew
	( 0x5f0 , 0x5f2 , 125 ), # Hebrew
	( 0x5f3 , 0x5f4 , 125 ), # Hebrew
	( 0x600 , 0x604 , 160 ), # Arabic
	( 0x605 , 0x605 , 998 ), # Common
	( 0x606 , 0x608 , 160 ), # Arabic
	( 0x609 , 0x60a , 160 ), # Arabic
	( 0x60b , 0x60b , 160 ), # Arabic
	( 0x60c , 0x60c , 998 ), # Common
	( 0x60d , 0x60d , 160 ), # Arabic
	( 0x60e , 0x60f , 160 ), # Arabic
	( 0x610 , 0x61a , 160 ), # Arabic
	( 0x61b , 0x61b , 998 ), # Common
	( 0x61c , 0x61c , 998 ), # Common
	( 0x61e , 0x61e , 160 ), # Arabic
	( 0x61f , 0x61f , 998 ), # Common
	( 0x620 , 0x63f , 160 ), # Arabic
	( 0x640 , 0x640 , 998 ), # Common
	( 0x641 , 0x64a , 160 ), # Arabic
	( 0x64b , 0x655 , 994 ), # Inherited
	( 0x656 , 0x65f , 160 ), # Arabic
	( 0x660 , 0x669 , 998 ), # Common
	( 0x66a , 0x66d , 160 ), # Arabic
	( 0x66e , 0x66f , 160 ), # Arabic
	( 0x670 , 0x670 , 994 ), # Inherited
	( 0x671 , 0x6d3 , 160 ), # Arabic
	( 0x6d4 , 0x6d4 , 160 ), # Arabic
	( 0x6d5 , 0x6d5 , 160 ), # Arabic
	( 0x6d6 , 0x6dc , 160 ), # Arabic
	( 0x6dd , 0x6dd , 998 ), # Common
	( 0x6de , 0x6de , 160 ), # Arabic
	( 0x6df , 0x6e4 , 160 ), # Arabic
	( 0x6e5 , 0x6e6 , 160 ), # Arabic
	( 0x6e7 , 0x6e8 , 160 ), # Arabic
	( 0x6e9 , 0x6e9 , 160 ), # Arabic
	( 0x6ea , 0x6ed , 160 ), # Arabic
	( 0x6ee , 0x6ef , 160 ), # Arabic
	( 0x6f0 , 0x6f9 , 160 ), # Arabic
	( 0x6fa , 0x6fc , 160 ), # Arabic
	( 0x6fd , 0x6fe , 160 ), # Arabic
	( 0x6ff , 0x6ff , 160 ), # Arabic
	( 0x700 , 0x70d , 135 ), # Syriac
	( 0x70f , 0x70f , 135 ), # Syriac
	( 0x710 , 0x710 , 135 ), # Syriac
	( 0x711 , 0x711 , 135 ), # Syriac
	( 0x712 , 0x72f , 135 ), # Syriac
	( 0x730 , 0x74a , 135 ), # Syriac
	( 0x74d , 0x74f , 135 ), # Syriac
	( 0x750 , 0x77f , 160 ), # Arabic
	( 0x780 , 0x7a5 , 170 ), # Thaana
	( 0x7a6 , 0x7b0 , 170 ), # Thaana
	( 0x7b1 , 0x7b1 , 170 ), # Thaana
	( 0x7c0 , 0x7c9 , 165 ), # Nko
	( 0x7ca , 0x7ea , 165 ), # Nko
	( 0x7eb , 0x7f3 , 165 ), # Nko
	( 0x7f4 , 0x7f5 , 165 ), # Nko
	( 0x7f6 , 0x7f6 , 165 ), # Nko
	( 0x7f7 , 0x7f9 , 165 ), # Nko
	( 0x7fa , 0x7fa , 165 ), # Nko
	( 0x800 , 0x815 , 123 ), # Samaritan
	( 0x816 , 0x819 , 123 ), # Samaritan
	( 0x81a , 0x81a , 123 ), # Samaritan
	( 0x81b , 0x823 , 123 ), # Samaritan
	( 0x824 , 0x824 , 123 ), # Samaritan
	( 0x825 , 0x827 , 123 ), # Samaritan
	( 0x828 , 0x828 , 123 ), # Samaritan
	( 0x829 , 0x82d , 123 ), # Samaritan
	( 0x830 , 0x83e , 123 ), # Samaritan
	( 0x840 , 0x858 , 140 ), # Mandaic
	( 0x859 , 0x85b , 140 ), # Mandaic
	( 0x85e , 0x85e , 140 ), # Mandaic
	( 0x8a0 , 0x8b2 , 160 ), # Arabic
	( 0x8e4 , 0x8ff , 160 ), # Arabic
	( 0x900 , 0x902 , 315 ), # Devanagari
	( 0x903 , 0x903 , 315 ), # Devanagari
	( 0x904 , 0x939 , 315 ), # Devanagari
	( 0x93a , 0x93a , 315 ), # Devanagari
	( 0x93b , 0x93b , 315 ), # Devanagari
	( 0x93c , 0x93c , 315 ), # Devanagari
	( 0x93d , 0x93d , 315 ), # Devanagari
	( 0x93e , 0x940 , 315 ), # Devanagari
	( 0x941 , 0x948 , 315 ), # Devanagari
	( 0x949 , 0x94c , 315 ), # Devanagari
	( 0x94d , 0x94d , 315 ), # Devanagari
	( 0x94e , 0x94f , 315 ), # Devanagari
	( 0x950 , 0x950 , 315 ), # Devanagari
	( 0x951 , 0x952 , 994 ), # Inherited
	( 0x953 , 0x957 , 315 ), # Devanagari
	( 0x958 , 0x961 , 315 ), # Devanagari
	( 0x962 , 0x963 , 315 ), # Devanagari
	( 0x964 , 0x965 , 998 ), # Common
	( 0x966 , 0x96f , 315 ), # Devanagari
	( 0x970 , 0x970 , 315 ), # Devanagari
	( 0x971 , 0x971 , 315 ), # Devanagari
	( 0x972 , 0x97f , 315 ), # Devanagari
	( 0x980 , 0x980 , 325 ), # Bengali
	( 0x981 , 0x981 , 325 ), # Bengali
	( 0x982 , 0x983 , 325 ), # Bengali
	( 0x985 , 0x98c , 325 ), # Bengali
	( 0x98f , 0x990 , 325 ), # Bengali
	( 0x993 , 0x9a8 , 325 ), # Bengali
	( 0x9aa , 0x9b0 , 325 ), # Bengali
	( 0x9b2 , 0x9b2 , 325 ), # Bengali
	( 0x9b6 , 0x9b9 , 325 ), # Bengali
	( 0x9bc , 0x9bc , 325 ), # Bengali
	( 0x9bd , 0x9bd , 325 ), # Bengali
	( 0x9be , 0x9c0 , 325 ), # Bengali
	( 0x9c1 , 0x9c4 , 325 ), # Bengali
	( 0x9c7 , 0x9c8 , 325 ), # Bengali
	( 0x9cb , 0x9cc , 325 ), # Bengali
	( 0x9cd , 0x9cd , 325 ), # Bengali
	( 0x9ce , 0x9ce , 325 ), # Bengali
	( 0x9d7 , 0x9d7 , 325 ), # Bengali
	( 0x9dc , 0x9dd , 325 ), # Bengali
	( 0x9df , 0x9e1 , 325 ), # Bengali
	( 0x9e2 , 0x9e3 , 325 ), # Bengali
	( 0x9e6 , 0x9ef , 325 ), # Bengali
	( 0x9f0 , 0x9f1 , 325 ), # Bengali
	( 0x9f2 , 0x9f3 , 325 ), # Bengali
	( 0x9f4 , 0x9f9 , 325 ), # Bengali
	( 0x9fa , 0x9fa , 325 ), # Bengali
	( 0x9fb , 0x9fb , 325 ), # Bengali
	( 0xa01 , 0xa02 , 310 ), # Gurmukhi
	( 0xa03 , 0xa03 , 310 ), # Gurmukhi
	( 0xa05 , 0xa0a , 310 ), # Gurmukhi
	( 0xa0f , 0xa10 , 310 ), # Gurmukhi
	( 0xa13 , 0xa28 , 310 ), # Gurmukhi
	( 0xa2a , 0xa30 , 310 ), # Gurmukhi
	( 0xa32 , 0xa33 , 310 ), # Gurmukhi
	( 0xa35 , 0xa36 , 310 ), # Gurmukhi
	( 0xa38 , 0xa39 , 310 ), # Gurmukhi
	( 0xa3c , 0xa3c , 310 ), # Gurmukhi
	( 0xa3e , 0xa40 , 310 ), # Gurmukhi
	( 0xa41 , 0xa42 , 310 ), # Gurmukhi
	( 0xa47 , 0xa48 , 310 ), # Gurmukhi
	( 0xa4b , 0xa4d , 310 ), # Gurmukhi
	( 0xa51 , 0xa51 , 310 ), # Gurmukhi
	( 0xa59 , 0xa5c , 310 ), # Gurmukhi
	( 0xa5e , 0xa5e , 310 ), # Gurmukhi
	( 0xa66 , 0xa6f , 310 ), # Gurmukhi
	( 0xa70 , 0xa71 , 310 ), # Gurmukhi
	( 0xa72 , 0xa74 , 310 ), # Gurmukhi
	( 0xa75 , 0xa75 , 310 ), # Gurmukhi
	( 0xa81 , 0xa82 , 320 ), # Gujarati
	( 0xa83 , 0xa83 , 320 ), # Gujarati
	( 0xa85 , 0xa8d , 320 ), # Gujarati
	( 0xa8f , 0xa91 , 320 ), # Gujarati
	( 0xa93 , 0xaa8 , 320 ), # Gujarati
	( 0xaaa , 0xab0 , 320 ), # Gujarati
	( 0xab2 , 0xab3 , 320 ), # Gujarati
	( 0xab5 , 0xab9 , 320 ), # Gujarati
	( 0xabc , 0xabc , 320 ), # Gujarati
	( 0xabd , 0xabd , 320 ), # Gujarati
	( 0xabe , 0xac0 , 320 ), # Gujarati
	( 0xac1 , 0xac5 , 320 ), # Gujarati
	( 0xac7 , 0xac8 , 320 ), # Gujarati
	( 0xac9 , 0xac9 , 320 ), # Gujarati
	( 0xacb , 0xacc , 320 ), # Gujarati
	( 0xacd , 0xacd , 320 ), # Gujarati
	( 0xad0 , 0xad0 , 320 ), # Gujarati
	( 0xae0 , 0xae1 , 320 ), # Gujarati
	( 0xae2 , 0xae3 , 320 ), # Gujarati
	( 0xae6 , 0xaef , 320 ), # Gujarati
	( 0xaf0 , 0xaf0 , 320 ), # Gujarati
	( 0xaf1 , 0xaf1 , 320 ), # Gujarati
	( 0xb01 , 0xb01 , 327 ), # Oriya
	( 0xb02 , 0xb03 , 327 ), # Oriya
	( 0xb05 , 0xb0c , 327 ), # Oriya
	( 0xb0f , 0xb10 , 327 ), # Oriya
	( 0xb13 , 0xb28 , 327 ), # Oriya
	( 0xb2a , 0xb30 , 327 ), # Oriya
	( 0xb32 , 0xb33 , 327 ), # Oriya
	( 0xb35 , 0xb39 , 327 ), # Oriya
	( 0xb3c , 0xb3c , 327 ), # Oriya
	( 0xb3d , 0xb3d , 327 ), # Oriya
	( 0xb3e , 0xb3e , 327 ), # Oriya
	( 0xb3f , 0xb3f , 327 ), # Oriya
	( 0xb40 , 0xb40 , 327 ), # Oriya
	( 0xb41 , 0xb44 , 327 ), # Oriya
	( 0xb47 , 0xb48 , 327 ), # Oriya
	( 0xb4b , 0xb4c , 327 ), # Oriya
	( 0xb4d , 0xb4d , 327 ), # Oriya
	( 0xb56 , 0xb56 , 327 ), # Oriya
	( 0xb57 , 0xb57 , 327 ), # Oriya
	( 0xb5c , 0xb5d , 327 ), # Oriya
	( 0xb5f , 0xb61 , 327 ), # Oriya
	( 0xb62 , 0xb63 , 327 ), # Oriya
	( 0xb66 , 0xb6f , 327 ), # Oriya
	( 0xb70 , 0xb70 , 327 ), # Oriya
	( 0xb71 , 0xb71 , 327 ), # Oriya
	( 0xb72 , 0xb77 , 327 ), # Oriya
	( 0xb82 , 0xb82 , 346 ), # Tamil
	( 0xb83 , 0xb83 , 346 ), # Tamil
	( 0xb85 , 0xb8a , 346 ), # Tamil
	( 0xb8e , 0xb90 , 346 ), # Tamil
	( 0xb92 , 0xb95 , 346 ), # Tamil
	( 0xb99 , 0xb9a , 346 ), # Tamil
	( 0xb9c , 0xb9c , 346 ), # Tamil
	( 0xb9e , 0xb9f , 346 ), # Tamil
	( 0xba3 , 0xba4 , 346 ), # Tamil
	( 0xba8 , 0xbaa , 346 ), # Tamil
	( 0xbae , 0xbb9 , 346 ), # Tamil
	( 0xbbe , 0xbbf , 346 ), # Tamil
	( 0xbc0 , 0xbc0 , 346 ), # Tamil
	( 0xbc1 , 0xbc2 , 346 ), # Tamil
	( 0xbc6 , 0xbc8 , 346 ), # Tamil
	( 0xbca , 0xbcc , 346 ), # Tamil
	( 0xbcd , 0xbcd , 346 ), # Tamil
	( 0xbd0 , 0xbd0 , 346 ), # Tamil
	( 0xbd7 , 0xbd7 , 346 ), # Tamil
	( 0xbe6 , 0xbef , 346 ), # Tamil
	( 0xbf0 , 0xbf2 , 346 ), # Tamil
	( 0xbf3 , 0xbf8 , 346 ), # Tamil
	( 0xbf9 , 0xbf9 , 346 ), # Tamil
	( 0xbfa , 0xbfa , 346 ), # Tamil
	( 0xc00 , 0xc00 , 340 ), # Telugu
	( 0xc01 , 0xc03 , 340 ), # Telugu
	( 0xc05 , 0xc0c , 340 ), # Telugu
	( 0xc0e , 0xc10 , 340 ), # Telugu
	( 0xc12 , 0xc28 , 340 ), # Telugu
	( 0xc2a , 0xc39 , 340 ), # Telugu
	( 0xc3d , 0xc3d , 340 ), # Telugu
	( 0xc3e , 0xc40 , 340 ), # Telugu
	( 0xc41 , 0xc44 , 340 ), # Telugu
	( 0xc46 , 0xc48 , 340 ), # Telugu
	( 0xc4a , 0xc4d , 340 ), # Telugu
	( 0xc55 , 0xc56 , 340 ), # Telugu
	( 0xc58 , 0xc59 , 340 ), # Telugu
	( 0xc60 , 0xc61 , 340 ), # Telugu
	( 0xc62 , 0xc63 , 340 ), # Telugu
	( 0xc66 , 0xc6f , 340 ), # Telugu
	( 0xc78 , 0xc7e , 340 ), # Telugu
	( 0xc7f , 0xc7f , 340 ), # Telugu
	( 0xc81 , 0xc81 , 345 ), # Kannada
	( 0xc82 , 0xc83 , 345 ), # Kannada
	( 0xc85 , 0xc8c , 345 ), # Kannada
	( 0xc8e , 0xc90 , 345 ), # Kannada
	( 0xc92 , 0xca8 , 345 ), # Kannada
	( 0xcaa , 0xcb3 , 345 ), # Kannada
	( 0xcb5 , 0xcb9 , 345 ), # Kannada
	( 0xcbc , 0xcbc , 345 ), # Kannada
	( 0xcbd , 0xcbd , 345 ), # Kannada
	( 0xcbe , 0xcbe , 345 ), # Kannada
	( 0xcbf , 0xcbf , 345 ), # Kannada
	( 0xcc0 , 0xcc4 , 345 ), # Kannada
	( 0xcc6 , 0xcc6 , 345 ), # Kannada
	( 0xcc7 , 0xcc8 , 345 ), # Kannada
	( 0xcca , 0xccb , 345 ), # Kannada
	( 0xccc , 0xccd , 345 ), # Kannada
	( 0xcd5 , 0xcd6 , 345 ), # Kannada
	( 0xcde , 0xcde , 345 ), # Kannada
	( 0xce0 , 0xce1 , 345 ), # Kannada
	( 0xce2 , 0xce3 , 345 ), # Kannada
	( 0xce6 , 0xcef , 345 ), # Kannada
	( 0xcf1 , 0xcf2 , 345 ), # Kannada
	( 0xd01 , 0xd01 , 347 ), # Malayalam
	( 0xd02 , 0xd03 , 347 ), # Malayalam
	( 0xd05 , 0xd0c , 347 ), # Malayalam
	( 0xd0e , 0xd10 , 347 ), # Malayalam
	( 0xd12 , 0xd3a , 347 ), # Malayalam
	( 0xd3d , 0xd3d , 347 ), # Malayalam
	( 0xd3e , 0xd40 , 347 ), # Malayalam
	( 0xd41 , 0xd44 , 347 ), # Malayalam
	( 0xd46 , 0xd48 , 347 ), # Malayalam
	( 0xd4a , 0xd4c , 347 ), # Malayalam
	( 0xd4d , 0xd4d , 347 ), # Malayalam
	( 0xd4e , 0xd4e , 347 ), # Malayalam
	( 0xd57 , 0xd57 , 347 ), # Malayalam
	( 0xd60 , 0xd61 , 347 ), # Malayalam
	( 0xd62 , 0xd63 , 347 ), # Malayalam
	( 0xd66 , 0xd6f , 347 ), # Malayalam
	( 0xd70 , 0xd75 , 347 ), # Malayalam
	( 0xd79 , 0xd79 , 347 ), # Malayalam
	( 0xd7a , 0xd7f , 347 ), # Malayalam
	( 0xd82 , 0xd83 , 348 ), # Sinhala
	( 0xd85 , 0xd96 , 348 ), # Sinhala
	( 0xd9a , 0xdb1 , 348 ), # Sinhala
	( 0xdb3 , 0xdbb , 348 ), # Sinhala
	( 0xdbd , 0xdbd , 348 ), # Sinhala
	( 0xdc0 , 0xdc6 , 348 ), # Sinhala
	( 0xdca , 0xdca , 348 ), # Sinhala
	( 0xdcf , 0xdd1 , 348 ), # Sinhala
	( 0xdd2 , 0xdd4 , 348 ), # Sinhala
	( 0xdd6 , 0xdd6 , 348 ), # Sinhala
	( 0xdd8 , 0xddf , 348 ), # Sinhala
	( 0xde6 , 0xdef , 348 ), # Sinhala
	( 0xdf2 , 0xdf3 , 348 ), # Sinhala
	( 0xdf4 , 0xdf4 , 348 ), # Sinhala
	( 0xe01 , 0xe30 , 352 ), # Thai
	( 0xe31 , 0xe31 , 352 ), # Thai
	( 0xe32 , 0xe33 , 352 ), # Thai
	( 0xe34 , 0xe3a , 352 ), # Thai
	( 0xe3f , 0xe3f , 998 ), # Common
	( 0xe40 , 0xe45 , 352 ), # Thai
	( 0xe46 , 0xe46 , 352 ), # Thai
	( 0xe47 , 0xe4e , 352 ), # Thai
	( 0xe4f , 0xe4f , 352 ), # Thai
	( 0xe50 , 0xe59 , 352 ), # Thai
	( 0xe5a , 0xe5b , 352 ), # Thai
	( 0xe81 , 0xe82 , 356 ), # Lao
	( 0xe84 , 0xe84 , 356 ), # Lao
	( 0xe87 , 0xe88 , 356 ), # Lao
	( 0xe8a , 0xe8a , 356 ), # Lao
	( 0xe8d , 0xe8d , 356 ), # Lao
	( 0xe94 , 0xe97 , 356 ), # Lao
	( 0xe99 , 0xe9f , 356 ), # Lao
	( 0xea1 , 0xea3 , 356 ), # Lao
	( 0xea5 , 0xea5 , 356 ), # Lao
	( 0xea7 , 0xea7 , 356 ), # Lao
	( 0xeaa , 0xeab , 356 ), # Lao
	( 0xead , 0xeb0 , 356 ), # Lao
	( 0xeb1 , 0xeb1 , 356 ), # Lao
	( 0xeb2 , 0xeb3 , 356 ), # Lao
	( 0xeb4 , 0xeb9 , 356 ), # Lao
	( 0xebb , 0xebc , 356 ), # Lao
	( 0xebd , 0xebd , 356 ), # Lao
	( 0xec0 , 0xec4 , 356 ), # Lao
	( 0xec6 , 0xec6 , 356 ), # Lao
	( 0xec8 , 0xecd , 356 ), # Lao
	( 0xed0 , 0xed9 , 356 ), # Lao
	( 0xedc , 0xedf , 356 ), # Lao
	( 0xf00 , 0xf00 , 330 ), # Tibetan
	( 0xf01 , 0xf03 , 330 ), # Tibetan
	( 0xf04 , 0xf12 , 330 ), # Tibetan
	( 0xf13 , 0xf13 , 330 ), # Tibetan
	( 0xf14 , 0xf14 , 330 ), # Tibetan
	( 0xf15 , 0xf17 , 330 ), # Tibetan
	( 0xf18 , 0xf19 , 330 ), # Tibetan
	( 0xf1a , 0xf1f , 330 ), # Tibetan
	( 0xf20 , 0xf29 , 330 ), # Tibetan
	( 0xf2a , 0xf33 , 330 ), # Tibetan
	( 0xf34 , 0xf34 , 330 ), # Tibetan
	( 0xf35 , 0xf35 , 330 ), # Tibetan
	( 0xf36 , 0xf36 , 330 ), # Tibetan
	( 0xf37 , 0xf37 , 330 ), # Tibetan
	( 0xf38 , 0xf38 , 330 ), # Tibetan
	( 0xf39 , 0xf39 , 330 ), # Tibetan
	( 0xf3a , 0xf3a , 330 ), # Tibetan
	( 0xf3b , 0xf3b , 330 ), # Tibetan
	( 0xf3c , 0xf3c , 330 ), # Tibetan
	( 0xf3d , 0xf3d , 330 ), # Tibetan
	( 0xf3e , 0xf3f , 330 ), # Tibetan
	( 0xf40 , 0xf47 , 330 ), # Tibetan
	( 0xf49 , 0xf6c , 330 ), # Tibetan
	( 0xf71 , 0xf7e , 330 ), # Tibetan
	( 0xf7f , 0xf7f , 330 ), # Tibetan
	( 0xf80 , 0xf84 , 330 ), # Tibetan
	( 0xf85 , 0xf85 , 330 ), # Tibetan
	( 0xf86 , 0xf87 , 330 ), # Tibetan
	( 0xf88 , 0xf8c , 330 ), # Tibetan
	( 0xf8d , 0xf97 , 330 ), # Tibetan
	( 0xf99 , 0xfbc , 330 ), # Tibetan
	( 0xfbe , 0xfc5 , 330 ), # Tibetan
	( 0xfc6 , 0xfc6 , 330 ), # Tibetan
	( 0xfc7 , 0xfcc , 330 ), # Tibetan
	( 0xfce , 0xfcf , 330 ), # Tibetan
	( 0xfd0 , 0xfd4 , 330 ), # Tibetan
	( 0xfd5 , 0xfd8 , 998 ), # Common
	( 0xfd9 , 0xfda , 330 ), # Tibetan
	( 0x1000 , 0x102a , 350 ), # Myanmar
	( 0x102b , 0x102c , 350 ), # Myanmar
	( 0x102d , 0x1030 , 350 ), # Myanmar
	( 0x1031 , 0x1031 , 350 ), # Myanmar
	( 0x1032 , 0x1037 , 350 ), # Myanmar
	( 0x1038 , 0x1038 , 350 ), # Myanmar
	( 0x1039 , 0x103a , 350 ), # Myanmar
	( 0x103b , 0x103c , 350 ), # Myanmar
	( 0x103d , 0x103e , 350 ), # Myanmar
	( 0x103f , 0x103f , 350 ), # Myanmar
	( 0x1040 , 0x1049 , 350 ), # Myanmar
	( 0x104a , 0x104f , 350 ), # Myanmar
	( 0x1050 , 0x1055 , 350 ), # Myanmar
	( 0x1056 , 0x1057 , 350 ), # Myanmar
	( 0x1058 , 0x1059 , 350 ), # Myanmar
	( 0x105a , 0x105d , 350 ), # Myanmar
	( 0x105e , 0x1060 , 350 ), # Myanmar
	( 0x1061 , 0x1061 , 350 ), # Myanmar
	( 0x1062 , 0x1064 , 350 ), # Myanmar
	( 0x1065 , 0x1066 , 350 ), # Myanmar
	( 0x1067 , 0x106d , 350 ), # Myanmar
	( 0x106e , 0x1070 , 350 ), # Myanmar
	( 0x1071 , 0x1074 , 350 ), # Myanmar
	( 0x1075 , 0x1081 , 350 ), # Myanmar
	( 0x1082 , 0x1082 , 350 ), # Myanmar
	( 0x1083 , 0x1084 , 350 ), # Myanmar
	( 0x1085 , 0x1086 , 350 ), # Myanmar
	( 0x1087 , 0x108c , 350 ), # Myanmar
	( 0x108d , 0x108d , 350 ), # Myanmar
	( 0x108e , 0x108e , 350 ), # Myanmar
	( 0x108f , 0x108f , 350 ), # Myanmar
	( 0x1090 , 0x1099 , 350 ), # Myanmar
	( 0x109a , 0x109c , 350 ), # Myanmar
	( 0x109d , 0x109d , 350 ), # Myanmar
	( 0x109e , 0x109f , 350 ), # Myanmar
	( 0x10a0 , 0x10c5 , 240 ), # Georgian
	( 0x10c7 , 0x10c7 , 240 ), # Georgian
	( 0x10cd , 0x10cd , 240 ), # Georgian
	( 0x10d0 , 0x10fa , 240 ), # Georgian
	( 0x10fb , 0x10fb , 998 ), # Common
	( 0x10fc , 0x10fc , 240 ), # Georgian
	( 0x10fd , 0x10ff , 240 ), # Georgian
	( 0x1100 , 0x11ff , 286 ), # Hangul
	( 0x1200 , 0x1248 , 430 ), # Ethiopic
	( 0x124a , 0x124d , 430 ), # Ethiopic
	( 0x1250 , 0x1256 , 430 ), # Ethiopic
	( 0x1258 , 0x1258 , 430 ), # Ethiopic
	( 0x125a , 0x125d , 430 ), # Ethiopic
	( 0x1260 , 0x1288 , 430 ), # Ethiopic
	( 0x128a , 0x128d , 430 ), # Ethiopic
	( 0x1290 , 0x12b0 , 430 ), # Ethiopic
	( 0x12b2 , 0x12b5 , 430 ), # Ethiopic
	( 0x12b8 , 0x12be , 430 ), # Ethiopic
	( 0x12c0 , 0x12c0 , 430 ), # Ethiopic
	( 0x12c2 , 0x12c5 , 430 ), # Ethiopic
	( 0x12c8 , 0x12d6 , 430 ), # Ethiopic
	( 0x12d8 , 0x1310 , 430 ), # Ethiopic
	( 0x1312 , 0x1315 , 430 ), # Ethiopic
	( 0x1318 , 0x135a , 430 ), # Ethiopic
	( 0x135d , 0x135f , 430 ), # Ethiopic
	( 0x1360 , 0x1368 , 430 ), # Ethiopic
	( 0x1369 , 0x137c , 430 ), # Ethiopic
	( 0x1380 , 0x138f , 430 ), # Ethiopic
	( 0x1390 , 0x1399 , 430 ), # Ethiopic
	( 0x13a0 , 0x13f4 , 445 ), # Cherokee
	( 0x1400 , 0x1400 , 440 ), # Canadian_Aboriginal
	( 0x1401 , 0x166c , 440 ), # Canadian_Aboriginal
	( 0x166d , 0x166e , 440 ), # Canadian_Aboriginal
	( 0x166f , 0x167f , 440 ), # Canadian_Aboriginal
	( 0x1680 , 0x1680 , 212 ), # Ogham
	( 0x1681 , 0x169a , 212 ), # Ogham
	( 0x169b , 0x169b , 212 ), # Ogham
	( 0x169c , 0x169c , 212 ), # Ogham
	( 0x16a0 , 0x16ea , 211 ), # Runic
	( 0x16eb , 0x16ed , 998 ), # Common
	( 0x16ee , 0x16f0 , 211 ), # Runic
	( 0x16f1 , 0x16f8 , 211 ), # Runic
	( 0x1700 , 0x170c , 370 ), # Tagalog
	( 0x170e , 0x1711 , 370 ), # Tagalog
	( 0x1712 , 0x1714 , 370 ), # Tagalog
	( 0x1720 , 0x1731 , 371 ), # Hanunoo
	( 0x1732 , 0x1734 , 371 ), # Hanunoo
	( 0x1735 , 0x1736 , 998 ), # Common
	( 0x1740 , 0x1751 , 372 ), # Buhid
	( 0x1752 , 0x1753 , 372 ), # Buhid
	( 0x1760 , 0x176c , 373 ), # Tagbanwa
	( 0x176e , 0x1770 , 373 ), # Tagbanwa
	( 0x1772 , 0x1773 , 373 ), # Tagbanwa
	( 0x1780 , 0x17b3 , 355 ), # Khmer
	( 0x17b4 , 0x17b5 , 355 ), # Khmer
	( 0x17b6 , 0x17b6 , 355 ), # Khmer
	( 0x17b7 , 0x17bd , 355 ), # Khmer
	( 0x17be , 0x17c5 , 355 ), # Khmer
	( 0x17c6 , 0x17c6 , 355 ), # Khmer
	( 0x17c7 , 0x17c8 , 355 ), # Khmer
	( 0x17c9 , 0x17d3 , 355 ), # Khmer
	( 0x17d4 , 0x17d6 , 355 ), # Khmer
	( 0x17d7 , 0x17d7 , 355 ), # Khmer
	( 0x17d8 , 0x17da , 355 ), # Khmer
	( 0x17db , 0x17db , 355 ), # Khmer
	( 0x17dc , 0x17dc , 355 ), # Khmer
	( 0x17dd , 0x17dd , 355 ), # Khmer
	( 0x17e0 , 0x17e9 , 355 ), # Khmer
	( 0x17f0 , 0x17f9 , 355 ), # Khmer
	( 0x1800 , 0x1801 , 145 ), # Mongolian
	( 0x1802 , 0x1803 , 998 ), # Common
	( 0x1804 , 0x1804 , 145 ), # Mongolian
	( 0x1805 , 0x1805 , 998 ), # Common
	( 0x1806 , 0x1806 , 145 ), # Mongolian
	( 0x1807 , 0x180a , 145 ), # Mongolian
	( 0x180b , 0x180d , 145 ), # Mongolian
	( 0x180e , 0x180e , 145 ), # Mongolian
	( 0x1810 , 0x1819 , 145 ), # Mongolian
	( 0x1820 , 0x1842 , 145 ), # Mongolian
	( 0x1843 , 0x1843 , 145 ), # Mongolian
	( 0x1844 , 0x1877 , 145 ), # Mongolian
	( 0x1880 , 0x18a8 , 145 ), # Mongolian
	( 0x18a9 , 0x18a9 , 145 ), # Mongolian
	( 0x18aa , 0x18aa , 145 ), # Mongolian
	( 0x18b0 , 0x18f5 , 440 ), # Canadian_Aboriginal
	( 0x1900 , 0x191e , 336 ), # Limbu
	( 0x1920 , 0x1922 , 336 ), # Limbu
	( 0x1923 , 0x1926 , 336 ), # Limbu
	( 0x1927 , 0x1928 , 336 ), # Limbu
	( 0x1929 , 0x192b , 336 ), # Limbu
	( 0x1930 , 0x1931 , 336 ), # Limbu
	( 0x1932 , 0x1932 , 336 ), # Limbu
	( 0x1933 , 0x1938 , 336 ), # Limbu
	( 0x1939 , 0x193b , 336 ), # Limbu
	( 0x1940 , 0x1940 , 336 ), # Limbu
	( 0x1944 , 0x1945 , 336 ), # Limbu
	( 0x1946 , 0x194f , 336 ), # Limbu
	( 0x1950 , 0x196d , 353 ), # Tai_Le
	( 0x1970 , 0x1974 , 353 ), # Tai_Le
	( 0x1980 , 0x19ab , 354 ), # New_Tai_Lue
	( 0x19b0 , 0x19c0 , 354 ), # New_Tai_Lue
	( 0x19c1 , 0x19c7 , 354 ), # New_Tai_Lue
	( 0x19c8 , 0x19c9 , 354 ), # New_Tai_Lue
	( 0x19d0 , 0x19d9 , 354 ), # New_Tai_Lue
	( 0x19da , 0x19da , 354 ), # New_Tai_Lue
	( 0x19de , 0x19df , 354 ), # New_Tai_Lue
	( 0x19e0 , 0x19ff , 355 ), # Khmer
	( 0x1a00 , 0x1a16 , 367 ), # Buginese
	( 0x1a17 , 0x1a18 , 367 ), # Buginese
	( 0x1a19 , 0x1a1a , 367 ), # Buginese
	( 0x1a1b , 0x1a1b , 367 ), # Buginese
	( 0x1a1e , 0x1a1f , 367 ), # Buginese
	( 0x1ab0 , 0x1abd , 994 ), # Inherited
	( 0x1abe , 0x1abe , 994 ), # Inherited
	( 0x1b00 , 0x1b03 , 360 ), # Balinese
	( 0x1b04 , 0x1b04 , 360 ), # Balinese
	( 0x1b05 , 0x1b33 , 360 ), # Balinese
	( 0x1b34 , 0x1b34 , 360 ), # Balinese
	( 0x1b35 , 0x1b35 , 360 ), # Balinese
	( 0x1b36 , 0x1b3a , 360 ), # Balinese
	( 0x1b3b , 0x1b3b , 360 ), # Balinese
	( 0x1b3c , 0x1b3c , 360 ), # Balinese
	( 0x1b3d , 0x1b41 , 360 ), # Balinese
	( 0x1b42 , 0x1b42 , 360 ), # Balinese
	( 0x1b43 , 0x1b44 , 360 ), # Balinese
	( 0x1b45 , 0x1b4b , 360 ), # Balinese
	( 0x1b50 , 0x1b59 , 360 ), # Balinese
	( 0x1b5a , 0x1b60 , 360 ), # Balinese
	( 0x1b61 , 0x1b6a , 360 ), # Balinese
	( 0x1b6b , 0x1b73 , 360 ), # Balinese
	( 0x1b74 , 0x1b7c , 360 ), # Balinese
	( 0x1b80 , 0x1b81 , 362 ), # Sundanese
	( 0x1b82 , 0x1b82 , 362 ), # Sundanese
	( 0x1b83 , 0x1ba0 , 362 ), # Sundanese
	( 0x1ba1 , 0x1ba1 , 362 ), # Sundanese
	( 0x1ba2 , 0x1ba5 , 362 ), # Sundanese
	( 0x1ba6 , 0x1ba7 , 362 ), # Sundanese
	( 0x1ba8 , 0x1ba9 , 362 ), # Sundanese
	( 0x1baa , 0x1baa , 362 ), # Sundanese
	( 0x1bab , 0x1bad , 362 ), # Sundanese
	( 0x1bae , 0x1baf , 362 ), # Sundanese
	( 0x1bb0 , 0x1bb9 , 362 ), # Sundanese
	( 0x1bba , 0x1bbf , 362 ), # Sundanese
	( 0x1bc0 , 0x1be5 , 365 ), # Batak
	( 0x1be6 , 0x1be6 , 365 ), # Batak
	( 0x1be7 , 0x1be7 , 365 ), # Batak
	( 0x1be8 , 0x1be9 , 365 ), # Batak
	( 0x1bea , 0x1bec , 365 ), # Batak
	( 0x1bed , 0x1bed , 365 ), # Batak
	( 0x1bee , 0x1bee , 365 ), # Batak
	( 0x1bef , 0x1bf1 , 365 ), # Batak
	( 0x1bf2 , 0x1bf3 , 365 ), # Batak
	( 0x1bfc , 0x1bff , 365 ), # Batak
	( 0x1c00 , 0x1c23 , 335 ), # Lepcha
	( 0x1c24 , 0x1c2b , 335 ), # Lepcha
	( 0x1c2c , 0x1c33 , 335 ), # Lepcha
	( 0x1c34 , 0x1c35 , 335 ), # Lepcha
	( 0x1c36 , 0x1c37 , 335 ), # Lepcha
	( 0x1c3b , 0x1c3f , 335 ), # Lepcha
	( 0x1c40 , 0x1c49 , 335 ), # Lepcha
	( 0x1c4d , 0x1c4f , 335 ), # Lepcha
	( 0x1c50 , 0x1c59 , 261 ), # Ol_Chiki
	( 0x1c5a , 0x1c77 , 261 ), # Ol_Chiki
	( 0x1c78 , 0x1c7d , 261 ), # Ol_Chiki
	( 0x1c7e , 0x1c7f , 261 ), # Ol_Chiki
	( 0x1cc0 , 0x1cc7 , 362 ), # Sundanese
	( 0x1cd0 , 0x1cd2 , 994 ), # Inherited
	( 0x1cd3 , 0x1cd3 , 998 ), # Common
	( 0x1cd4 , 0x1ce0 , 994 ), # Inherited
	( 0x1ce1 , 0x1ce1 , 998 ), # Common
	( 0x1ce2 , 0x1ce8 , 994 ), # Inherited
	( 0x1ce9 , 0x1cec , 998 ), # Common
	( 0x1ced , 0x1ced , 994 ), # Inherited
	( 0x1cee , 0x1cf1 , 998 ), # Common
	( 0x1cf2 , 0x1cf3 , 998 ), # Common
	( 0x1cf4 , 0x1cf4 , 994 ), # Inherited
	( 0x1cf5 , 0x1cf6 , 998 ), # Common
	( 0x1cf8 , 0x1cf9 , 994 ), # Inherited
	( 0x1d00 , 0x1d25 , 215 ), # Latin
	( 0x1d26 , 0x1d2a , 200 ), # Greek
	( 0x1d2b , 0x1d2b , 220 ), # Cyrillic
	( 0x1d2c , 0x1d5c , 215 ), # Latin
	( 0x1d5d , 0x1d61 , 200 ), # Greek
	( 0x1d62 , 0x1d65 , 215 ), # Latin
	( 0x1d66 , 0x1d6a , 200 ), # Greek
	( 0x1d6b , 0x1d77 , 215 ), # Latin
	( 0x1d78 , 0x1d78 , 220 ), # Cyrillic
	( 0x1d79 , 0x1d9a , 215 ), # Latin
	( 0x1d9b , 0x1dbe , 215 ), # Latin
	( 0x1dbf , 0x1dbf , 200 ), # Greek
	( 0x1dc0 , 0x1df5 , 994 ), # Inherited
	( 0x1dfc , 0x1dff , 994 ), # Inherited
	( 0x1e00 , 0x1eff , 215 ), # Latin
	( 0x1f00 , 0x1f15 , 200 ), # Greek
	( 0x1f18 , 0x1f1d , 200 ), # Greek
	( 0x1f20 , 0x1f45 , 200 ), # Greek
	( 0x1f48 , 0x1f4d , 200 ), # Greek
	( 0x1f50 , 0x1f57 , 200 ), # Greek
	( 0x1f59 , 0x1f59 , 200 ), # Greek
	( 0x1f5b , 0x1f5b , 200 ), # Greek
	( 0x1f5d , 0x1f5d , 200 ), # Greek
	( 0x1f5f , 0x1f7d , 200 ), # Greek
	( 0x1f80 , 0x1fb4 , 200 ), # Greek
	( 0x1fb6 , 0x1fbc , 200 ), # Greek
	( 0x1fbd , 0x1fbd , 200 ), # Greek
	( 0x1fbe , 0x1fbe , 200 ), # Greek
	( 0x1fbf , 0x1fc1 , 200 ), # Greek
	( 0x1fc2 , 0x1fc4 , 200 ), # Greek
	( 0x1fc6 , 0x1fcc , 200 ), # Greek
	( 0x1fcd , 0x1fcf , 200 ), # Greek
	( 0x1fd0 , 0x1fd3 , 200 ), # Greek
	( 0x1fd6 , 0x1fdb , 200 ), # Greek
	( 0x1fdd , 0x1fdf , 200 ), # Greek
	( 0x1fe0 , 0x1fec , 200 ), # Greek
	( 0x1fed , 0x1fef , 200 ), # Greek
	( 0x1ff2 , 0x1ff4 , 200 ), # Greek
	( 0x1ff6 , 0x1ffc , 200 ), # Greek
	( 0x1ffd , 0x1ffe , 200 ), # Greek
	( 0x2000 , 0x200a , 998 ), # Common
	( 0x200b , 0x200b , 998 ), # Common
	( 0x200c , 0x200d , 994 ), # Inherited
	( 0x200e , 0x200f , 998 ), # Common
	( 0x2010 , 0x2015 , 998 ), # Common
	( 0x2016 , 0x2017 , 998 ), # Common
	( 0x2018 , 0x2018 , 998 ), # Common
	( 0x2019 , 0x2019 , 998 ), # Common
	( 0x201a , 0x201a , 998 ), # Common
	( 0x201b , 0x201c , 998 ), # Common
	( 0x201d , 0x201d , 998 ), # Common
	( 0x201e , 0x201e , 998 ), # Common
	( 0x201f , 0x201f , 998 ), # Common
	( 0x2020 , 0x2027 , 998 ), # Common
	( 0x2028 , 0x2028 , 998 ), # Common
	( 0x2029 , 0x2029 , 998 ), # Common
	( 0x202a , 0x202e , 998 ), # Common
	( 0x202f , 0x202f , 998 ), # Common
	( 0x2030 , 0x2038 , 998 ), # Common
	( 0x2039 , 0x2039 , 998 ), # Common
	( 0x203a , 0x203a , 998 ), # Common
	( 0x203b , 0x203e , 998 ), # Common
	( 0x203f , 0x2040 , 998 ), # Common
	( 0x2041 , 0x2043 , 998 ), # Common
	( 0x2044 , 0x2044 , 998 ), # Common
	( 0x2045 , 0x2045 , 998 ), # Common
	( 0x2046 , 0x2046 , 998 ), # Common
	( 0x2047 , 0x2051 , 998 ), # Common
	( 0x2052 , 0x2052 , 998 ), # Common
	( 0x2053 , 0x2053 , 998 ), # Common
	( 0x2054 , 0x2054 , 998 ), # Common
	( 0x2055 , 0x205e , 998 ), # Common
	( 0x205f , 0x205f , 998 ), # Common
	( 0x2060 , 0x2064 , 998 ), # Common
	( 0x2066 , 0x206f , 998 ), # Common
	( 0x2070 , 0x2070 , 998 ), # Common
	( 0x2071 , 0x2071 , 215 ), # Latin
	( 0x2074 , 0x2079 , 998 ), # Common
	( 0x207a , 0x207c , 998 ), # Common
	( 0x207d , 0x207d , 998 ), # Common
	( 0x207e , 0x207e , 998 ), # Common
	( 0x207f , 0x207f , 215 ), # Latin
	( 0x2080 , 0x2089 , 998 ), # Common
	( 0x208a , 0x208c , 998 ), # Common
	( 0x208d , 0x208d , 998 ), # Common
	( 0x208e , 0x208e , 998 ), # Common
	( 0x2090 , 0x209c , 215 ), # Latin
	( 0x20a0 , 0x20bd , 998 ), # Common
	( 0x20d0 , 0x20dc , 994 ), # Inherited
	( 0x20dd , 0x20e0 , 994 ), # Inherited
	( 0x20e1 , 0x20e1 , 994 ), # Inherited
	( 0x20e2 , 0x20e4 , 994 ), # Inherited
	( 0x20e5 , 0x20f0 , 994 ), # Inherited
	( 0x2100 , 0x2101 , 998 ), # Common
	( 0x2102 , 0x2102 , 998 ), # Common
	( 0x2103 , 0x2106 , 998 ), # Common
	( 0x2107 , 0x2107 , 998 ), # Common
	( 0x2108 , 0x2109 , 998 ), # Common
	( 0x210a , 0x2113 , 998 ), # Common
	( 0x2114 , 0x2114 , 998 ), # Common
	( 0x2115 , 0x2115 , 998 ), # Common
	( 0x2116 , 0x2117 , 998 ), # Common
	( 0x2118 , 0x2118 , 998 ), # Common
	( 0x2119 , 0x211d , 998 ), # Common
	( 0x211e , 0x2123 , 998 ), # Common
	( 0x2124 , 0x2124 , 998 ), # Common
	( 0x2125 , 0x2125 , 998 ), # Common
	( 0x2126 , 0x2126 , 200 ), # Greek
	( 0x2127 , 0x2127 , 998 ), # Common
	( 0x2128 , 0x2128 , 998 ), # Common
	( 0x2129 , 0x2129 , 998 ), # Common
	( 0x212a , 0x212b , 215 ), # Latin
	( 0x212c , 0x212d , 998 ), # Common
	( 0x212e , 0x212e , 998 ), # Common
	( 0x212f , 0x2131 , 998 ), # Common
	( 0x2132 , 0x2132 , 215 ), # Latin
	( 0x2133 , 0x2134 , 998 ), # Common
	( 0x2135 , 0x2138 , 998 ), # Common
	( 0x2139 , 0x2139 , 998 ), # Common
	( 0x213a , 0x213b , 998 ), # Common
	( 0x213c , 0x213f , 998 ), # Common
	( 0x2140 , 0x2144 , 998 ), # Common
	( 0x2145 , 0x2149 , 998 ), # Common
	( 0x214a , 0x214a , 998 ), # Common
	( 0x214b , 0x214b , 998 ), # Common
	( 0x214c , 0x214d , 998 ), # Common
	( 0x214e , 0x214e , 215 ), # Latin
	( 0x214f , 0x214f , 998 ), # Common
	( 0x2150 , 0x215f , 998 ), # Common
	( 0x2160 , 0x2182 , 215 ), # Latin
	( 0x2183 , 0x2184 , 215 ), # Latin
	( 0x2185 , 0x2188 , 215 ), # Latin
	( 0x2189 , 0x2189 , 998 ), # Common
	( 0x2190 , 0x2194 , 998 ), # Common
	( 0x2195 , 0x2199 , 998 ), # Common
	( 0x219a , 0x219b , 998 ), # Common
	( 0x219c , 0x219f , 998 ), # Common
	( 0x21a0 , 0x21a0 , 998 ), # Common
	( 0x21a1 , 0x21a2 , 998 ), # Common
	( 0x21a3 , 0x21a3 , 998 ), # Common
	( 0x21a4 , 0x21a5 , 998 ), # Common
	( 0x21a6 , 0x21a6 , 998 ), # Common
	( 0x21a7 , 0x21ad , 998 ), # Common
	( 0x21ae , 0x21ae , 998 ), # Common
	( 0x21af , 0x21cd , 998 ), # Common
	( 0x21ce , 0x21cf , 998 ), # Common
	( 0x21d0 , 0x21d1 , 998 ), # Common
	( 0x21d2 , 0x21d2 , 998 ), # Common
	( 0x21d3 , 0x21d3 , 998 ), # Common
	( 0x21d4 , 0x21d4 , 998 ), # Common
	( 0x21d5 , 0x21f3 , 998 ), # Common
	( 0x21f4 , 0x22ff , 998 ), # Common
	( 0x2300 , 0x2307 , 998 ), # Common
	( 0x2308 , 0x2308 , 998 ), # Common
	( 0x2309 , 0x2309 , 998 ), # Common
	( 0x230a , 0x230a , 998 ), # Common
	( 0x230b , 0x230b , 998 ), # Common
	( 0x230c , 0x231f , 998 ), # Common
	( 0x2320 , 0x2321 , 998 ), # Common
	( 0x2322 , 0x2328 , 998 ), # Common
	( 0x2329 , 0x2329 , 998 ), # Common
	( 0x232a , 0x232a , 998 ), # Common
	( 0x232b , 0x237b , 998 ), # Common
	( 0x237c , 0x237c , 998 ), # Common
	( 0x237d , 0x239a , 998 ), # Common
	( 0x239b , 0x23b3 , 998 ), # Common
	( 0x23b4 , 0x23db , 998 ), # Common
	( 0x23dc , 0x23e1 , 998 ), # Common
	( 0x23e2 , 0x23fa , 998 ), # Common
	( 0x2400 , 0x2426 , 998 ), # Common
	( 0x2440 , 0x244a , 998 ), # Common
	( 0x2460 , 0x249b , 998 ), # Common
	( 0x249c , 0x24e9 , 998 ), # Common
	( 0x24ea , 0x24ff , 998 ), # Common
	( 0x2500 , 0x25b6 , 998 ), # Common
	( 0x25b7 , 0x25b7 , 998 ), # Common
	( 0x25b8 , 0x25c0 , 998 ), # Common
	( 0x25c1 , 0x25c1 , 998 ), # Common
	( 0x25c2 , 0x25f7 , 998 ), # Common
	( 0x25f8 , 0x25ff , 998 ), # Common
	( 0x2600 , 0x266e , 998 ), # Common
	( 0x266f , 0x266f , 998 ), # Common
	( 0x2670 , 0x2767 , 998 ), # Common
	( 0x2768 , 0x2768 , 998 ), # Common
	( 0x2769 , 0x2769 , 998 ), # Common
	( 0x276a , 0x276a , 998 ), # Common
	( 0x276b , 0x276b , 998 ), # Common
	( 0x276c , 0x276c , 998 ), # Common
	( 0x276d , 0x276d , 998 ), # Common
	( 0x276e , 0x276e , 998 ), # Common
	( 0x276f , 0x276f , 998 ), # Common
	( 0x2770 , 0x2770 , 998 ), # Common
	( 0x2771 , 0x2771 , 998 ), # Common
	( 0x2772 , 0x2772 , 998 ), # Common
	( 0x2773 , 0x2773 , 998 ), # Common
	( 0x2774 , 0x2774 , 998 ), # Common
	( 0x2775 , 0x2775 , 998 ), # Common
	( 0x2776 , 0x2793 , 998 ), # Common
	( 0x2794 , 0x27bf , 998 ), # Common
	( 0x27c0 , 0x27c4 , 998 ), # Common
	( 0x27c5 , 0x27c5 , 998 ), # Common
	( 0x27c6 , 0x27c6 , 998 ), # Common
	( 0x27c7 , 0x27e5 , 998 ), # Common
	( 0x27e6 , 0x27e6 , 998 ), # Common
	( 0x27e7 , 0x27e7 , 998 ), # Common
	( 0x27e8 , 0x27e8 , 998 ), # Common
	( 0x27e9 , 0x27e9 , 998 ), # Common
	( 0x27ea , 0x27ea , 998 ), # Common
	( 0x27eb , 0x27eb , 998 ), # Common
	( 0x27ec , 0x27ec , 998 ), # Common
	( 0x27ed , 0x27ed , 998 ), # Common
	( 0x27ee , 0x27ee , 998 ), # Common
	( 0x27ef , 0x27ef , 998 ), # Common
	( 0x27f0 , 0x27ff , 998 ), # Common
	( 0x2800 , 0x28ff , 570 ), # Braille
	( 0x2900 , 0x2982 , 998 ), # Common
	( 0x2983 , 0x2983 , 998 ), # Common
	( 0x2984 , 0x2984 , 998 ), # Common
	( 0x2985 , 0x2985 , 998 ), # Common
	( 0x2986 , 0x2986 , 998 ), # Common
	( 0x2987 , 0x2987 , 998 ), # Common
	( 0x2988 , 0x2988 , 998 ), # Common
	( 0x2989 , 0x2989 , 998 ), # Common
	( 0x298a , 0x298a , 998 ), # Common
	( 0x298b , 0x298b , 998 ), # Common
	( 0x298c , 0x298c , 998 ), # Common
	( 0x298d , 0x298d , 998 ), # Common
	( 0x298e , 0x298e , 998 ), # Common
	( 0x298f , 0x298f , 998 ), # Common
	( 0x2990 , 0x2990 , 998 ), # Common
	( 0x2991 , 0x2991 , 998 ), # Common
	( 0x2992 , 0x2992 , 998 ), # Common
	( 0x2993 , 0x2993 , 998 ), # Common
	( 0x2994 , 0x2994 , 998 ), # Common
	( 0x2995 , 0x2995 , 998 ), # Common
	( 0x2996 , 0x2996 , 998 ), # Common
	( 0x2997 , 0x2997 , 998 ), # Common
	( 0x2998 , 0x2998 , 998 ), # Common
	( 0x2999 , 0x29d7 , 998 ), # Common
	( 0x29d8 , 0x29d8 , 998 ), # Common
	( 0x29d9 , 0x29d9 , 998 ), # Common
	( 0x29da , 0x29da , 998 ), # Common
	( 0x29db , 0x29db , 998 ), # Common
	( 0x29dc , 0x29fb , 998 ), # Common
	( 0x29fc , 0x29fc , 998 ), # Common
	( 0x29fd , 0x29fd , 998 ), # Common
	( 0x29fe , 0x2aff , 998 ), # Common
	( 0x2b00 , 0x2b2f , 998 ), # Common
	( 0x2b30 , 0x2b44 , 998 ), # Common
	( 0x2b45 , 0x2b46 , 998 ), # Common
	( 0x2b47 , 0x2b4c , 998 ), # Common
	( 0x2b4d , 0x2b73 , 998 ), # Common
	( 0x2b76 , 0x2b95 , 998 ), # Common
	( 0x2b98 , 0x2bb9 , 998 ), # Common
	( 0x2bbd , 0x2bc8 , 998 ), # Common
	( 0x2bca , 0x2bd1 , 998 ), # Common
	( 0x2c00 , 0x2c2e , 225 ), # Glagolitic
	( 0x2c30 , 0x2c5e , 225 ), # Glagolitic
	( 0x2c60 , 0x2c7b , 215 ), # Latin
	( 0x2c7c , 0x2c7d , 215 ), # Latin
	( 0x2c7e , 0x2c7f , 215 ), # Latin
	( 0x2c80 , 0x2ce4 , 204 ), # Coptic
	( 0x2ce5 , 0x2cea , 204 ), # Coptic
	( 0x2ceb , 0x2cee , 204 ), # Coptic
	( 0x2cef , 0x2cf1 , 204 ), # Coptic
	( 0x2cf2 , 0x2cf3 , 204 ), # Coptic
	( 0x2cf9 , 0x2cfc , 204 ), # Coptic
	( 0x2cfd , 0x2cfd , 204 ), # Coptic
	( 0x2cfe , 0x2cff , 204 ), # Coptic
	( 0x2d00 , 0x2d25 , 240 ), # Georgian
	( 0x2d27 , 0x2d27 , 240 ), # Georgian
	( 0x2d2d , 0x2d2d , 240 ), # Georgian
	( 0x2d30 , 0x2d67 , 120 ), # Tifinagh
	( 0x2d6f , 0x2d6f , 120 ), # Tifinagh
	( 0x2d70 , 0x2d70 , 120 ), # Tifinagh
	( 0x2d7f , 0x2d7f , 120 ), # Tifinagh
	( 0x2d80 , 0x2d96 , 430 ), # Ethiopic
	( 0x2da0 , 0x2da6 , 430 ), # Ethiopic
	( 0x2da8 , 0x2dae , 430 ), # Ethiopic
	( 0x2db0 , 0x2db6 , 430 ), # Ethiopic
	( 0x2db8 , 0x2dbe , 430 ), # Ethiopic
	( 0x2dc0 , 0x2dc6 , 430 ), # Ethiopic
	( 0x2dc8 , 0x2dce , 430 ), # Ethiopic
	( 0x2dd0 , 0x2dd6 , 430 ), # Ethiopic
	( 0x2dd8 , 0x2dde , 430 ), # Ethiopic
	( 0x2de0 , 0x2dff , 220 ), # Cyrillic
	( 0x2e00 , 0x2e01 , 998 ), # Common
	( 0x2e02 , 0x2e02 , 998 ), # Common
	( 0x2e03 , 0x2e03 , 998 ), # Common
	( 0x2e04 , 0x2e04 , 998 ), # Common
	( 0x2e05 , 0x2e05 , 998 ), # Common
	( 0x2e06 , 0x2e08 , 998 ), # Common
	( 0x2e09 , 0x2e09 , 998 ), # Common
	( 0x2e0a , 0x2e0a , 998 ), # Common
	( 0x2e0b , 0x2e0b , 998 ), # Common
	( 0x2e0c , 0x2e0c , 998 ), # Common
	( 0x2e0d , 0x2e0d , 998 ), # Common
	( 0x2e0e , 0x2e16 , 998 ), # Common
	( 0x2e17 , 0x2e17 , 998 ), # Common
	( 0x2e18 , 0x2e19 , 998 ), # Common
	( 0x2e1a , 0x2e1a , 998 ), # Common
	( 0x2e1b , 0x2e1b , 998 ), # Common
	( 0x2e1c , 0x2e1c , 998 ), # Common
	( 0x2e1d , 0x2e1d , 998 ), # Common
	( 0x2e1e , 0x2e1f , 998 ), # Common
	( 0x2e20 , 0x2e20 , 998 ), # Common
	( 0x2e21 , 0x2e21 , 998 ), # Common
	( 0x2e22 , 0x2e22 , 998 ), # Common
	( 0x2e23 , 0x2e23 , 998 ), # Common
	( 0x2e24 , 0x2e24 , 998 ), # Common
	( 0x2e25 , 0x2e25 , 998 ), # Common
	( 0x2e26 , 0x2e26 , 998 ), # Common
	( 0x2e27 , 0x2e27 , 998 ), # Common
	( 0x2e28 , 0x2e28 , 998 ), # Common
	( 0x2e29 , 0x2e29 , 998 ), # Common
	( 0x2e2a , 0x2e2e , 998 ), # Common
	( 0x2e2f , 0x2e2f , 998 ), # Common
	( 0x2e30 , 0x2e39 , 998 ), # Common
	( 0x2e3a , 0x2e3b , 998 ), # Common
	( 0x2e3c , 0x2e3f , 998 ), # Common
	( 0x2e40 , 0x2e40 , 998 ), # Common
	( 0x2e41 , 0x2e41 , 998 ), # Common
	( 0x2e42 , 0x2e42 , 998 ), # Common
	( 0x2e80 , 0x2e99 , 500 ), # Han
	( 0x2e9b , 0x2ef3 , 500 ), # Han
	( 0x2f00 , 0x2fd5 , 500 ), # Han
	( 0x2ff0 , 0x2ffb , 998 ), # Common
	( 0x3000 , 0x3000 , 998 ), # Common
	( 0x3001 , 0x3003 , 998 ), # Common
	( 0x3004 , 0x3004 , 998 ), # Common
	( 0x3005 , 0x3005 , 500 ), # Han
	( 0x3006 , 0x3006 , 998 ), # Common
	( 0x3007 , 0x3007 , 500 ), # Han
	( 0x3008 , 0x3008 , 998 ), # Common
	( 0x3009 , 0x3009 , 998 ), # Common
	( 0x300a , 0x300a , 998 ), # Common
	( 0x300b , 0x300b , 998 ), # Common
	( 0x300c , 0x300c , 998 ), # Common
	( 0x300d , 0x300d , 998 ), # Common
	( 0x300e , 0x300e , 998 ), # Common
	( 0x300f , 0x300f , 998 ), # Common
	( 0x3010 , 0x3010 , 998 ), # Common
	( 0x3011 , 0x3011 , 998 ), # Common
	( 0x3012 , 0x3013 , 998 ), # Common
	( 0x3014 , 0x3014 , 998 ), # Common
	( 0x3015 , 0x3015 , 998 ), # Common
	( 0x3016 , 0x3016 , 998 ), # Common
	( 0x3017 , 0x3017 , 998 ), # Common
	( 0x3018 , 0x3018 , 998 ), # Common
	( 0x3019 , 0x3019 , 998 ), # Common
	( 0x301a , 0x301a , 998 ), # Common
	( 0x301b , 0x301b , 998 ), # Common
	( 0x301c , 0x301c , 998 ), # Common
	( 0x301d , 0x301d , 998 ), # Common
	( 0x301e , 0x301f , 998 ), # Common
	( 0x3020 , 0x3020 , 998 ), # Common
	( 0x3021 , 0x3029 , 500 ), # Han
	( 0x302a , 0x302d , 994 ), # Inherited
	( 0x302e , 0x302f , 286 ), # Hangul
	( 0x3030 , 0x3030 , 998 ), # Common
	( 0x3031 , 0x3035 , 998 ), # Common
	( 0x3036 , 0x3037 , 998 ), # Common
	( 0x3038 , 0x303a , 500 ), # Han
	( 0x303b , 0x303b , 500 ), # Han
	( 0x303c , 0x303c , 998 ), # Common
	( 0x303d , 0x303d , 998 ), # Common
	( 0x303e , 0x303f , 998 ), # Common
	( 0x3041 , 0x3096 , 410 ), # Hiragana
	( 0x3099 , 0x309a , 994 ), # Inherited
	( 0x309b , 0x309c , 998 ), # Common
	( 0x309d , 0x309e , 410 ), # Hiragana
	( 0x309f , 0x309f , 410 ), # Hiragana
	( 0x30a0 , 0x30a0 , 998 ), # Common
	( 0x30a1 , 0x30fa , 411 ), # Katakana
	( 0x30fb , 0x30fb , 998 ), # Common
	( 0x30fc , 0x30fc , 998 ), # Common
	( 0x30fd , 0x30fe , 411 ), # Katakana
	( 0x30ff , 0x30ff , 411 ), # Katakana
	( 0x3105 , 0x312d , 285 ), # Bopomofo
	( 0x3131 , 0x318e , 286 ), # Hangul
	( 0x3190 , 0x3191 , 998 ), # Common
	( 0x3192 , 0x3195 , 998 ), # Common
	( 0x3196 , 0x319f , 998 ), # Common
	( 0x31a0 , 0x31ba , 285 ), # Bopomofo
	( 0x31c0 , 0x31e3 , 998 ), # Common
	( 0x31f0 , 0x31ff , 411 ), # Katakana
	( 0x3200 , 0x321e , 286 ), # Hangul
	( 0x3220 , 0x3229 , 998 ), # Common
	( 0x322a , 0x3247 , 998 ), # Common
	( 0x3248 , 0x324f , 998 ), # Common
	( 0x3250 , 0x3250 , 998 ), # Common
	( 0x3251 , 0x325f , 998 ), # Common
	( 0x3260 , 0x327e , 286 ), # Hangul
	( 0x327f , 0x327f , 998 ), # Common
	( 0x3280 , 0x3289 , 998 ), # Common
	( 0x328a , 0x32b0 , 998 ), # Common
	( 0x32b1 , 0x32bf , 998 ), # Common
	( 0x32c0 , 0x32cf , 998 ), # Common
	( 0x32d0 , 0x32fe , 411 ), # Katakana
	( 0x3300 , 0x3357 , 411 ), # Katakana
	( 0x3358 , 0x33ff , 998 ), # Common
	( 0x3400 , 0x4db5 , 500 ), # Han
	( 0x4dc0 , 0x4dff , 998 ), # Common
	( 0x4e00 , 0x9fcc , 500 ), # Han
	( 0xa000 , 0xa014 , 460 ), # Yi
	( 0xa015 , 0xa015 , 460 ), # Yi
	( 0xa016 , 0xa48c , 460 ), # Yi
	( 0xa490 , 0xa4c6 , 460 ), # Yi
	( 0xa4d0 , 0xa4f7 , 399 ), # Lisu
	( 0xa4f8 , 0xa4fd , 399 ), # Lisu
	( 0xa4fe , 0xa4ff , 399 ), # Lisu
	( 0xa500 , 0xa60b , 470 ), # Vai
	( 0xa60c , 0xa60c , 470 ), # Vai
	( 0xa60d , 0xa60f , 470 ), # Vai
	( 0xa610 , 0xa61f , 470 ), # Vai
	( 0xa620 , 0xa629 , 470 ), # Vai
	( 0xa62a , 0xa62b , 470 ), # Vai
	( 0xa640 , 0xa66d , 220 ), # Cyrillic
	( 0xa66e , 0xa66e , 220 ), # Cyrillic
	( 0xa66f , 0xa66f , 220 ), # Cyrillic
	( 0xa670 , 0xa672 , 220 ), # Cyrillic
	( 0xa673 , 0xa673 , 220 ), # Cyrillic
	( 0xa674 , 0xa67d , 220 ), # Cyrillic
	( 0xa67e , 0xa67e , 220 ), # Cyrillic
	( 0xa67f , 0xa67f , 220 ), # Cyrillic
	( 0xa680 , 0xa69b , 220 ), # Cyrillic
	( 0xa69c , 0xa69d , 220 ), # Cyrillic
	( 0xa69f , 0xa69f , 220 ), # Cyrillic
	( 0xa6a0 , 0xa6e5 , 435 ), # Bamum
	( 0xa6e6 , 0xa6ef , 435 ), # Bamum
	( 0xa6f0 , 0xa6f1 , 435 ), # Bamum
	( 0xa6f2 , 0xa6f7 , 435 ), # Bamum
	( 0xa700 , 0xa716 , 998 ), # Common
	( 0xa717 , 0xa71f , 998 ), # Common
	( 0xa720 , 0xa721 , 998 ), # Common
	( 0xa722 , 0xa76f , 215 ), # Latin
	( 0xa770 , 0xa770 , 215 ), # Latin
	( 0xa771 , 0xa787 , 215 ), # Latin
	( 0xa788 , 0xa788 , 998 ), # Common
	( 0xa789 , 0xa78a , 998 ), # Common
	( 0xa78b , 0xa78e , 215 ), # Latin
	( 0xa790 , 0xa7ad , 215 ), # Latin
	( 0xa7b0 , 0xa7b1 , 215 ), # Latin
	( 0xa7f7 , 0xa7f7 , 215 ), # Latin
	( 0xa7f8 , 0xa7f9 , 215 ), # Latin
	( 0xa7fa , 0xa7fa , 215 ), # Latin
	( 0xa7fb , 0xa7ff , 215 ), # Latin
	( 0xa800 , 0xa801 , 316 ), # Syloti_Nagri
	( 0xa802 , 0xa802 , 316 ), # Syloti_Nagri
	( 0xa803 , 0xa805 , 316 ), # Syloti_Nagri
	( 0xa806 , 0xa806 , 316 ), # Syloti_Nagri
	( 0xa807 , 0xa80a , 316 ), # Syloti_Nagri
	( 0xa80b , 0xa80b , 316 ), # Syloti_Nagri
	( 0xa80c , 0xa822 , 316 ), # Syloti_Nagri
	( 0xa823 , 0xa824 , 316 ), # Syloti_Nagri
	( 0xa825 , 0xa826 , 316 ), # Syloti_Nagri
	( 0xa827 , 0xa827 , 316 ), # Syloti_Nagri
	( 0xa828 , 0xa82b , 316 ), # Syloti_Nagri
	( 0xa830 , 0xa835 , 998 ), # Common
	( 0xa836 , 0xa837 , 998 ), # Common
	( 0xa838 , 0xa838 , 998 ), # Common
	( 0xa839 , 0xa839 , 998 ), # Common
	( 0xa840 , 0xa873 , 331 ), # Phags_Pa
	( 0xa874 , 0xa877 , 331 ), # Phags_Pa
	( 0xa880 , 0xa881 , 344 ), # Saurashtra
	( 0xa882 , 0xa8b3 , 344 ), # Saurashtra
	( 0xa8b4 , 0xa8c3 , 344 ), # Saurashtra
	( 0xa8c4 , 0xa8c4 , 344 ), # Saurashtra
	( 0xa8ce , 0xa8cf , 344 ), # Saurashtra
	( 0xa8d0 , 0xa8d9 , 344 ), # Saurashtra
	( 0xa8e0 , 0xa8f1 , 315 ), # Devanagari
	( 0xa8f2 , 0xa8f7 , 315 ), # Devanagari
	( 0xa8f8 , 0xa8fa , 315 ), # Devanagari
	( 0xa8fb , 0xa8fb , 315 ), # Devanagari
	( 0xa900 , 0xa909 , 357 ), # Kayah_Li
	( 0xa90a , 0xa925 , 357 ), # Kayah_Li
	( 0xa926 , 0xa92d , 357 ), # Kayah_Li
	( 0xa92e , 0xa92e , 998 ), # Common
	( 0xa92f , 0xa92f , 357 ), # Kayah_Li
	( 0xa930 , 0xa946 , 363 ), # Rejang
	( 0xa947 , 0xa951 , 363 ), # Rejang
	( 0xa952 , 0xa953 , 363 ), # Rejang
	( 0xa95f , 0xa95f , 363 ), # Rejang
	( 0xa960 , 0xa97c , 286 ), # Hangul
	( 0xa980 , 0xa982 , 361 ), # Javanese
	( 0xa983 , 0xa983 , 361 ), # Javanese
	( 0xa984 , 0xa9b2 , 361 ), # Javanese
	( 0xa9b3 , 0xa9b3 , 361 ), # Javanese
	( 0xa9b4 , 0xa9b5 , 361 ), # Javanese
	( 0xa9b6 , 0xa9b9 , 361 ), # Javanese
	( 0xa9ba , 0xa9bb , 361 ), # Javanese
	( 0xa9bc , 0xa9bc , 361 ), # Javanese
	( 0xa9bd , 0xa9c0 , 361 ), # Javanese
	( 0xa9c1 , 0xa9cd , 361 ), # Javanese
	( 0xa9cf , 0xa9cf , 998 ), # Common
	( 0xa9d0 , 0xa9d9 , 361 ), # Javanese
	( 0xa9de , 0xa9df , 361 ), # Javanese
	( 0xa9e0 , 0xa9e4 , 350 ), # Myanmar
	( 0xa9e5 , 0xa9e5 , 350 ), # Myanmar
	( 0xa9e6 , 0xa9e6 , 350 ), # Myanmar
	( 0xa9e7 , 0xa9ef , 350 ), # Myanmar
	( 0xa9f0 , 0xa9f9 , 350 ), # Myanmar
	( 0xa9fa , 0xa9fe , 350 ), # Myanmar
	( 0xaa00 , 0xaa28 , 358 ), # Cham
	( 0xaa29 , 0xaa2e , 358 ), # Cham
	( 0xaa2f , 0xaa30 , 358 ), # Cham
	( 0xaa31 , 0xaa32 , 358 ), # Cham
	( 0xaa33 , 0xaa34 , 358 ), # Cham
	( 0xaa35 , 0xaa36 , 358 ), # Cham
	( 0xaa40 , 0xaa42 , 358 ), # Cham
	( 0xaa43 , 0xaa43 , 358 ), # Cham
	( 0xaa44 , 0xaa4b , 358 ), # Cham
	( 0xaa4c , 0xaa4c , 358 ), # Cham
	( 0xaa4d , 0xaa4d , 358 ), # Cham
	( 0xaa50 , 0xaa59 , 358 ), # Cham
	( 0xaa5c , 0xaa5f , 358 ), # Cham
	( 0xaa60 , 0xaa6f , 350 ), # Myanmar
	( 0xaa70 , 0xaa70 , 350 ), # Myanmar
	( 0xaa71 , 0xaa76 , 350 ), # Myanmar
	( 0xaa77 , 0xaa79 , 350 ), # Myanmar
	( 0xaa7a , 0xaa7a , 350 ), # Myanmar
	( 0xaa7b , 0xaa7b , 350 ), # Myanmar
	( 0xaa7c , 0xaa7c , 350 ), # Myanmar
	( 0xaa7d , 0xaa7d , 350 ), # Myanmar
	( 0xaa7e , 0xaa7f , 350 ), # Myanmar
	( 0xaa80 , 0xaaaf , 359 ), # Tai_Viet
	( 0xaab0 , 0xaab0 , 359 ), # Tai_Viet
	( 0xaab1 , 0xaab1 , 359 ), # Tai_Viet
	( 0xaab2 , 0xaab4 , 359 ), # Tai_Viet
	( 0xaab5 , 0xaab6 , 359 ), # Tai_Viet
	( 0xaab7 , 0xaab8 , 359 ), # Tai_Viet
	( 0xaab9 , 0xaabd , 359 ), # Tai_Viet
	( 0xaabe , 0xaabf , 359 ), # Tai_Viet
	( 0xaac0 , 0xaac0 , 359 ), # Tai_Viet
	( 0xaac1 , 0xaac1 , 359 ), # Tai_Viet
	( 0xaac2 , 0xaac2 , 359 ), # Tai_Viet
	( 0xaadb , 0xaadc , 359 ), # Tai_Viet
	( 0xaadd , 0xaadd , 359 ), # Tai_Viet
	( 0xaade , 0xaadf , 359 ), # Tai_Viet
	( 0xaae0 , 0xaaea , 337 ), # Meetei_Mayek
	( 0xaaeb , 0xaaeb , 337 ), # Meetei_Mayek
	( 0xaaec , 0xaaed , 337 ), # Meetei_Mayek
	( 0xaaee , 0xaaef , 337 ), # Meetei_Mayek
	( 0xaaf0 , 0xaaf1 , 337 ), # Meetei_Mayek
	( 0xaaf2 , 0xaaf2 , 337 ), # Meetei_Mayek
	( 0xaaf3 , 0xaaf4 , 337 ), # Meetei_Mayek
	( 0xaaf5 , 0xaaf5 , 337 ), # Meetei_Mayek
	( 0xaaf6 , 0xaaf6 , 337 ), # Meetei_Mayek
	( 0xab01 , 0xab06 , 430 ), # Ethiopic
	( 0xab09 , 0xab0e , 430 ), # Ethiopic
	( 0xab11 , 0xab16 , 430 ), # Ethiopic
	( 0xab20 , 0xab26 , 430 ), # Ethiopic
	( 0xab28 , 0xab2e , 430 ), # Ethiopic
	( 0xab30 , 0xab5a , 215 ), # Latin
	( 0xab5b , 0xab5b , 998 ), # Common
	( 0xab5c , 0xab5f , 215 ), # Latin
	( 0xab64 , 0xab64 , 215 ), # Latin
	( 0xab65 , 0xab65 , 200 ), # Greek
	( 0xabc0 , 0xabe2 , 337 ), # Meetei_Mayek
	( 0xabe3 , 0xabe4 , 337 ), # Meetei_Mayek
	( 0xabe5 , 0xabe5 , 337 ), # Meetei_Mayek
	( 0xabe6 , 0xabe7 , 337 ), # Meetei_Mayek
	( 0xabe8 , 0xabe8 , 337 ), # Meetei_Mayek
	( 0xabe9 , 0xabea , 337 ), # Meetei_Mayek
	( 0xabeb , 0xabeb , 337 ), # Meetei_Mayek
	( 0xabec , 0xabec , 337 ), # Meetei_Mayek
	( 0xabed , 0xabed , 337 ), # Meetei_Mayek
	( 0xabf0 , 0xabf9 , 337 ), # Meetei_Mayek
	( 0xac00 , 0xd7a3 , 286 ), # Hangul
	( 0xd7b0 , 0xd7c6 , 286 ), # Hangul
	( 0xd7cb , 0xd7fb , 286 ), # Hangul
	( 0xf900 , 0xfa6d , 500 ), # Han
	( 0xfa70 , 0xfad9 , 500 ), # Han
	( 0xfb00 , 0xfb06 , 215 ), # Latin
	( 0xfb13 , 0xfb17 , 230 ), # Armenian
	( 0xfb1d , 0xfb1d , 125 ), # Hebrew
	( 0xfb1e , 0xfb1e , 125 ), # Hebrew
	( 0xfb1f , 0xfb28 , 125 ), # Hebrew
	( 0xfb29 , 0xfb29 , 125 ), # Hebrew
	( 0xfb2a , 0xfb36 , 125 ), # Hebrew
	( 0xfb38 , 0xfb3c , 125 ), # Hebrew
	( 0xfb3e , 0xfb3e , 125 ), # Hebrew
	( 0xfb40 , 0xfb41 , 125 ), # Hebrew
	( 0xfb43 , 0xfb44 , 125 ), # Hebrew
	( 0xfb46 , 0xfb4f , 125 ), # Hebrew
	( 0xfb50 , 0xfbb1 , 160 ), # Arabic
	( 0xfbb2 , 0xfbc1 , 160 ), # Arabic
	( 0xfbd3 , 0xfd3d , 160 ), # Arabic
	( 0xfd3e , 0xfd3e , 998 ), # Common
	( 0xfd3f , 0xfd3f , 998 ), # Common
	( 0xfd50 , 0xfd8f , 160 ), # Arabic
	( 0xfd92 , 0xfdc7 , 160 ), # Arabic
	( 0xfdf0 , 0xfdfb , 160 ), # Arabic
	( 0xfdfc , 0xfdfc , 160 ), # Arabic
	( 0xfdfd , 0xfdfd , 160 ), # Arabic
	( 0xfe00 , 0xfe0f , 994 ), # Inherited
	( 0xfe10 , 0xfe16 , 998 ), # Common
	( 0xfe17 , 0xfe17 , 998 ), # Common
	( 0xfe18 , 0xfe18 , 998 ), # Common
	( 0xfe19 , 0xfe19 , 998 ), # Common
	( 0xfe20 , 0xfe2d , 994 ), # Inherited
	( 0xfe30 , 0xfe30 , 998 ), # Common
	( 0xfe31 , 0xfe32 , 998 ), # Common
	( 0xfe33 , 0xfe34 , 998 ), # Common
	( 0xfe35 , 0xfe35 , 998 ), # Common
	( 0xfe36 , 0xfe36 , 998 ), # Common
	( 0xfe37 , 0xfe37 , 998 ), # Common
	( 0xfe38 , 0xfe38 , 998 ), # Common
	( 0xfe39 , 0xfe39 , 998 ), # Common
	( 0xfe3a , 0xfe3a , 998 ), # Common
	( 0xfe3b , 0xfe3b , 998 ), # Common
	( 0xfe3c , 0xfe3c , 998 ), # Common
	( 0xfe3d , 0xfe3d , 998 ), # Common
	( 0xfe3e , 0xfe3e , 998 ), # Common
	( 0xfe3f , 0xfe3f , 998 ), # Common
	( 0xfe40 , 0xfe40 , 998 ), # Common
	( 0xfe41 , 0xfe41 , 998 ), # Common
	( 0xfe42 , 0xfe42 , 998 ), # Common
	( 0xfe43 , 0xfe43 , 998 ), # Common
	( 0xfe44 , 0xfe44 , 998 ), # Common
	( 0xfe45 , 0xfe46 , 998 ), # Common
	( 0xfe47 , 0xfe47 , 998 ), # Common
	( 0xfe48 , 0xfe48 , 998 ), # Common
	( 0xfe49 , 0xfe4c , 998 ), # Common
	( 0xfe4d , 0xfe4f , 998 ), # Common
	( 0xfe50 , 0xfe52 , 998 ), # Common
	( 0xfe54 , 0xfe57 , 998 ), # Common
	( 0xfe58 , 0xfe58 , 998 ), # Common
	( 0xfe59 , 0xfe59 , 998 ), # Common
	( 0xfe5a , 0xfe5a , 998 ), # Common
	( 0xfe5b , 0xfe5b , 998 ), # Common
	( 0xfe5c , 0xfe5c , 998 ), # Common
	( 0xfe5d , 0xfe5d , 998 ), # Common
	( 0xfe5e , 0xfe5e , 998 ), # Common
	( 0xfe5f , 0xfe61 , 998 ), # Common
	( 0xfe62 , 0xfe62 , 998 ), # Common
	( 0xfe63 , 0xfe63 , 998 ), # Common
	( 0xfe64 , 0xfe66 , 998 ), # Common
	( 0xfe68 , 0xfe68 , 998 ), # Common
	( 0xfe69 , 0xfe69 , 998 ), # Common
	( 0xfe6a , 0xfe6b , 998 ), # Common
	( 0xfe70 , 0xfe74 , 160 ), # Arabic
	( 0xfe76 , 0xfefc , 160 ), # Arabic
	( 0xfeff , 0xfeff , 998 ), # Common
	( 0xff01 , 0xff03 , 998 ), # Common
	( 0xff04 , 0xff04 , 998 ), # Common
	( 0xff05 , 0xff07 , 998 ), # Common
	( 0xff08 , 0xff08 , 998 ), # Common
	( 0xff09 , 0xff09 , 998 ), # Common
	( 0xff0a , 0xff0a , 998 ), # Common
	( 0xff0b , 0xff0b , 998 ), # Common
	( 0xff0c , 0xff0c , 998 ), # Common
	( 0xff0d , 0xff0d , 998 ), # Common
	( 0xff0e , 0xff0f , 998 ), # Common
	( 0xff10 , 0xff19 , 998 ), # Common
	( 0xff1a , 0xff1b , 998 ), # Common
	( 0xff1c , 0xff1e , 998 ), # Common
	( 0xff1f , 0xff20 , 998 ), # Common
	( 0xff21 , 0xff3a , 215 ), # Latin
	( 0xff3b , 0xff3b , 998 ), # Common
	( 0xff3c , 0xff3c , 998 ), # Common
	( 0xff3d , 0xff3d , 998 ), # Common
	( 0xff3e , 0xff3e , 998 ), # Common
	( 0xff3f , 0xff3f , 998 ), # Common
	( 0xff40 , 0xff40 , 998 ), # Common
	( 0xff41 , 0xff5a , 215 ), # Latin
	( 0xff5b , 0xff5b , 998 ), # Common
	( 0xff5c , 0xff5c , 998 ), # Common
	( 0xff5d , 0xff5d , 998 ), # Common
	( 0xff5e , 0xff5e , 998 ), # Common
	( 0xff5f , 0xff5f , 998 ), # Common
	( 0xff60 , 0xff60 , 998 ), # Common
	( 0xff61 , 0xff61 , 998 ), # Common
	( 0xff62 , 0xff62 , 998 ), # Common
	( 0xff63 , 0xff63 , 998 ), # Common
	( 0xff64 , 0xff65 , 998 ), # Common
	( 0xff66 , 0xff6f , 411 ), # Katakana
	( 0xff70 , 0xff70 , 998 ), # Common
	( 0xff71 , 0xff9d , 411 ), # Katakana
	( 0xff9e , 0xff9f , 998 ), # Common
	( 0xffa0 , 0xffbe , 286 ), # Hangul
	( 0xffc2 , 0xffc7 , 286 ), # Hangul
	( 0xffca , 0xffcf , 286 ), # Hangul
	( 0xffd2 , 0xffd7 , 286 ), # Hangul
	( 0xffda , 0xffdc , 286 ), # Hangul
	( 0xffe0 , 0xffe1 , 998 ), # Common
	( 0xffe2 , 0xffe2 , 998 ), # Common
	( 0xffe3 , 0xffe3 , 998 ), # Common
	( 0xffe4 , 0xffe4 , 998 ), # Common
	( 0xffe5 , 0xffe6 , 998 ), # Common
	( 0xffe8 , 0xffe8 , 998 ), # Common
	( 0xffe9 , 0xffec , 998 ), # Common
	( 0xffed , 0xffee , 998 ), # Common
	( 0xfff9 , 0xfffb , 998 ), # Common
	( 0xfffc , 0xfffd , 998 ), # Common
	( 0x10000 , 0x1000b , 401 ), # Linear_B
	( 0x1000d , 0x10026 , 401 ), # Linear_B
	( 0x10028 , 0x1003a , 401 ), # Linear_B
	( 0x1003c , 0x1003d , 401 ), # Linear_B
	( 0x1003f , 0x1004d , 401 ), # Linear_B
	( 0x10050 , 0x1005d , 401 ), # Linear_B
	( 0x10080 , 0x100fa , 401 ), # Linear_B
	( 0x10100 , 0x10102 , 998 ), # Common
	( 0x10107 , 0x10133 , 998 ), # Common
	( 0x10137 , 0x1013f , 998 ), # Common
	( 0x10140 , 0x10174 , 200 ), # Greek
	( 0x10175 , 0x10178 , 200 ), # Greek
	( 0x10179 , 0x10189 , 200 ), # Greek
	( 0x1018a , 0x1018b , 200 ), # Greek
	( 0x1018c , 0x1018c , 200 ), # Greek
	( 0x10190 , 0x1019b , 998 ), # Common
	( 0x101a0 , 0x101a0 , 200 ), # Greek
	( 0x101d0 , 0x101fc , 998 ), # Common
	( 0x101fd , 0x101fd , 994 ), # Inherited
	( 0x10280 , 0x1029c , 202 ), # Lycian
	( 0x102a0 , 0x102d0 , 201 ), # Carian
	( 0x102e0 , 0x102e0 , 994 ), # Inherited
	( 0x102e1 , 0x102fb , 998 ), # Common
	( 0x10300 , 0x1031f , 210 ), # Old_Italic
	( 0x10320 , 0x10323 , 210 ), # Old_Italic
	( 0x10330 , 0x10340 , 206 ), # Gothic
	( 0x10341 , 0x10341 , 206 ), # Gothic
	( 0x10342 , 0x10349 , 206 ), # Gothic
	( 0x1034a , 0x1034a , 206 ), # Gothic
	( 0x10350 , 0x10375 , 227 ), # Old_Permic
	( 0x10376 , 0x1037a , 227 ), # Old_Permic
	( 0x10380 , 0x1039d , 40 ), # Ugaritic
	( 0x1039f , 0x1039f , 40 ), # Ugaritic
	( 0x103a0 , 0x103c3 , 30 ), # Old_Persian
	( 0x103c8 , 0x103cf , 30 ), # Old_Persian
	( 0x103d0 , 0x103d0 , 30 ), # Old_Persian
	( 0x103d1 , 0x103d5 , 30 ), # Old_Persian
	( 0x10400 , 0x1044f , 250 ), # Deseret
	( 0x10450 , 0x1047f , 281 ), # Shavian
	( 0x10480 , 0x1049d , 260 ), # Osmanya
	( 0x104a0 , 0x104a9 , 260 ), # Osmanya
	( 0x10500 , 0x10527 , 226 ), # Elbasan
	( 0x10530 , 0x10563 , 239 ), # Caucasian_Albanian
	( 0x1056f , 0x1056f , 239 ), # Caucasian_Albanian
	( 0x10600 , 0x10736 , 400 ), # Linear_A
	( 0x10740 , 0x10755 , 400 ), # Linear_A
	( 0x10760 , 0x10767 , 400 ), # Linear_A
	( 0x10800 , 0x10805 , 403 ), # Cypriot
	( 0x10808 , 0x10808 , 403 ), # Cypriot
	( 0x1080a , 0x10835 , 403 ), # Cypriot
	( 0x10837 , 0x10838 , 403 ), # Cypriot
	( 0x1083c , 0x1083c , 403 ), # Cypriot
	( 0x1083f , 0x1083f , 403 ), # Cypriot
	( 0x10840 , 0x10855 , 124 ), # Imperial_Aramaic
	( 0x10857 , 0x10857 , 124 ), # Imperial_Aramaic
	( 0x10858 , 0x1085f , 124 ), # Imperial_Aramaic
	( 0x10860 , 0x10876 , 126 ), # Palmyrene
	( 0x10877 , 0x10878 , 126 ), # Palmyrene
	( 0x10879 , 0x1087f , 126 ), # Palmyrene
	( 0x10880 , 0x1089e , 159 ), # Nabataean
	( 0x108a7 , 0x108af , 159 ), # Nabataean
	( 0x10900 , 0x10915 , 115 ), # Phoenician
	( 0x10916 , 0x1091b , 115 ), # Phoenician
	( 0x1091f , 0x1091f , 115 ), # Phoenician
	( 0x10920 , 0x10939 , 116 ), # Lydian
	( 0x1093f , 0x1093f , 116 ), # Lydian
	( 0x10980 , 0x1099f , 100 ), # Meroitic_Hieroglyphs
	( 0x109a0 , 0x109b7 , 101 ), # Meroitic_Cursive
	( 0x109be , 0x109bf , 101 ), # Meroitic_Cursive
	( 0x10a00 , 0x10a00 , 305 ), # Kharoshthi
	( 0x10a01 , 0x10a03 , 305 ), # Kharoshthi
	( 0x10a05 , 0x10a06 , 305 ), # Kharoshthi
	( 0x10a0c , 0x10a0f , 305 ), # Kharoshthi
	( 0x10a10 , 0x10a13 , 305 ), # Kharoshthi
	( 0x10a15 , 0x10a17 , 305 ), # Kharoshthi
	( 0x10a19 , 0x10a33 , 305 ), # Kharoshthi
	( 0x10a38 , 0x10a3a , 305 ), # Kharoshthi
	( 0x10a3f , 0x10a3f , 305 ), # Kharoshthi
	( 0x10a40 , 0x10a47 , 305 ), # Kharoshthi
	( 0x10a50 , 0x10a58 , 305 ), # Kharoshthi
	( 0x10a60 , 0x10a7c , 105 ), # Old_South_Arabian
	( 0x10a7d , 0x10a7e , 105 ), # Old_South_Arabian
	( 0x10a7f , 0x10a7f , 105 ), # Old_South_Arabian
	( 0x10a80 , 0x10a9c , 106 ), # Old_North_Arabian
	( 0x10a9d , 0x10a9f , 106 ), # Old_North_Arabian
	( 0x10ac0 , 0x10ac7 , 139 ), # Manichaean
	( 0x10ac8 , 0x10ac8 , 139 ), # Manichaean
	( 0x10ac9 , 0x10ae4 , 139 ), # Manichaean
	( 0x10ae5 , 0x10ae6 , 139 ), # Manichaean
	( 0x10aeb , 0x10aef , 139 ), # Manichaean
	( 0x10af0 , 0x10af6 , 139 ), # Manichaean
	( 0x10b00 , 0x10b35 , 134 ), # Avestan
	( 0x10b39 , 0x10b3f , 134 ), # Avestan
	( 0x10b40 , 0x10b55 , 130 ), # Inscriptional_Parthian
	( 0x10b58 , 0x10b5f , 130 ), # Inscriptional_Parthian
	( 0x10b60 , 0x10b72 , 131 ), # Inscriptional_Pahlavi
	( 0x10b78 , 0x10b7f , 131 ), # Inscriptional_Pahlavi
	( 0x10b80 , 0x10b91 , 132 ), # Psalter_Pahlavi
	( 0x10b99 , 0x10b9c , 132 ), # Psalter_Pahlavi
	( 0x10ba9 , 0x10baf , 132 ), # Psalter_Pahlavi
	( 0x10c00 , 0x10c48 , 175 ), # Old_Turkic
	( 0x10e60 , 0x10e7e , 160 ), # Arabic
	( 0x11000 , 0x11000 , 300 ), # Brahmi
	( 0x11001 , 0x11001 , 300 ), # Brahmi
	( 0x11002 , 0x11002 , 300 ), # Brahmi
	( 0x11003 , 0x11037 , 300 ), # Brahmi
	( 0x11038 , 0x11046 , 300 ), # Brahmi
	( 0x11047 , 0x1104d , 300 ), # Brahmi
	( 0x11052 , 0x11065 , 300 ), # Brahmi
	( 0x11066 , 0x1106f , 300 ), # Brahmi
	( 0x1107f , 0x1107f , 300 ), # Brahmi
	( 0x11080 , 0x11081 , 317 ), # Kaithi
	( 0x11082 , 0x11082 , 317 ), # Kaithi
	( 0x11083 , 0x110af , 317 ), # Kaithi
	( 0x110b0 , 0x110b2 , 317 ), # Kaithi
	( 0x110b3 , 0x110b6 , 317 ), # Kaithi
	( 0x110b7 , 0x110b8 , 317 ), # Kaithi
	( 0x110b9 , 0x110ba , 317 ), # Kaithi
	( 0x110bb , 0x110bc , 317 ), # Kaithi
	( 0x110bd , 0x110bd , 317 ), # Kaithi
	( 0x110be , 0x110c1 , 317 ), # Kaithi
	( 0x110d0 , 0x110e8 , 398 ), # Sora_Sompeng
	( 0x110f0 , 0x110f9 , 398 ), # Sora_Sompeng
	( 0x11100 , 0x11102 , 349 ), # Chakma
	( 0x11103 , 0x11126 , 349 ), # Chakma
	( 0x11127 , 0x1112b , 349 ), # Chakma
	( 0x1112c , 0x1112c , 349 ), # Chakma
	( 0x1112d , 0x11134 , 349 ), # Chakma
	( 0x11136 , 0x1113f , 349 ), # Chakma
	( 0x11140 , 0x11143 , 349 ), # Chakma
	( 0x11150 , 0x11172 , 314 ), # Mahajani
	( 0x11173 , 0x11173 , 314 ), # Mahajani
	( 0x11174 , 0x11175 , 314 ), # Mahajani
	( 0x11176 , 0x11176 , 314 ), # Mahajani
	( 0x11180 , 0x11181 , 319 ), # Sharada
	( 0x11182 , 0x11182 , 319 ), # Sharada
	( 0x11183 , 0x111b2 , 319 ), # Sharada
	( 0x111b3 , 0x111b5 , 319 ), # Sharada
	( 0x111b6 , 0x111be , 319 ), # Sharada
	( 0x111bf , 0x111c0 , 319 ), # Sharada
	( 0x111c1 , 0x111c4 , 319 ), # Sharada
	( 0x111c5 , 0x111c8 , 319 ), # Sharada
	( 0x111cd , 0x111cd , 319 ), # Sharada
	( 0x111d0 , 0x111d9 , 319 ), # Sharada
	( 0x111da , 0x111da , 319 ), # Sharada
	( 0x111e1 , 0x111f4 , 348 ), # Sinhala
	( 0x11200 , 0x11211 , 322 ), # Khojki
	( 0x11213 , 0x1122b , 322 ), # Khojki
	( 0x1122c , 0x1122e , 322 ), # Khojki
	( 0x1122f , 0x11231 , 322 ), # Khojki
	( 0x11232 , 0x11233 , 322 ), # Khojki
	( 0x11234 , 0x11234 , 322 ), # Khojki
	( 0x11235 , 0x11235 , 322 ), # Khojki
	( 0x11236 , 0x11237 , 322 ), # Khojki
	( 0x11238 , 0x1123d , 322 ), # Khojki
	( 0x112b0 , 0x112de , 318 ), # Khudawadi
	( 0x112df , 0x112df , 318 ), # Khudawadi
	( 0x112e0 , 0x112e2 , 318 ), # Khudawadi
	( 0x112e3 , 0x112ea , 318 ), # Khudawadi
	( 0x112f0 , 0x112f9 , 318 ), # Khudawadi
	( 0x11301 , 0x11301 , 343 ), # Grantha
	( 0x11302 , 0x11303 , 343 ), # Grantha
	( 0x11305 , 0x1130c , 343 ), # Grantha
	( 0x1130f , 0x11310 , 343 ), # Grantha
	( 0x11313 , 0x11328 , 343 ), # Grantha
	( 0x1132a , 0x11330 , 343 ), # Grantha
	( 0x11332 , 0x11333 , 343 ), # Grantha
	( 0x11335 , 0x11339 , 343 ), # Grantha
	( 0x1133c , 0x1133c , 343 ), # Grantha
	( 0x1133d , 0x1133d , 343 ), # Grantha
	( 0x1133e , 0x1133f , 343 ), # Grantha
	( 0x11340 , 0x11340 , 343 ), # Grantha
	( 0x11341 , 0x11344 , 343 ), # Grantha
	( 0x11347 , 0x11348 , 343 ), # Grantha
	( 0x1134b , 0x1134d , 343 ), # Grantha
	( 0x11357 , 0x11357 , 343 ), # Grantha
	( 0x1135d , 0x11361 , 343 ), # Grantha
	( 0x11362 , 0x11363 , 343 ), # Grantha
	( 0x11366 , 0x1136c , 343 ), # Grantha
	( 0x11370 , 0x11374 , 343 ), # Grantha
	( 0x11480 , 0x114af , 326 ), # Tirhuta
	( 0x114b0 , 0x114b2 , 326 ), # Tirhuta
	( 0x114b3 , 0x114b8 , 326 ), # Tirhuta
	( 0x114b9 , 0x114b9 , 326 ), # Tirhuta
	( 0x114ba , 0x114ba , 326 ), # Tirhuta
	( 0x114bb , 0x114be , 326 ), # Tirhuta
	( 0x114bf , 0x114c0 , 326 ), # Tirhuta
	( 0x114c1 , 0x114c1 , 326 ), # Tirhuta
	( 0x114c2 , 0x114c3 , 326 ), # Tirhuta
	( 0x114c4 , 0x114c5 , 326 ), # Tirhuta
	( 0x114c6 , 0x114c6 , 326 ), # Tirhuta
	( 0x114c7 , 0x114c7 , 326 ), # Tirhuta
	( 0x114d0 , 0x114d9 , 326 ), # Tirhuta
	( 0x11580 , 0x115ae , 302 ), # Siddham
	( 0x115af , 0x115b1 , 302 ), # Siddham
	( 0x115b2 , 0x115b5 , 302 ), # Siddham
	( 0x115b8 , 0x115bb , 302 ), # Siddham
	( 0x115bc , 0x115bd , 302 ), # Siddham
	( 0x115be , 0x115be , 302 ), # Siddham
	( 0x115bf , 0x115c0 , 302 ), # Siddham
	( 0x115c1 , 0x115c9 , 302 ), # Siddham
	( 0x11600 , 0x1162f , 324 ), # Modi
	( 0x11630 , 0x11632 , 324 ), # Modi
	( 0x11633 , 0x1163a , 324 ), # Modi
	( 0x1163b , 0x1163c , 324 ), # Modi
	( 0x1163d , 0x1163d , 324 ), # Modi
	( 0x1163e , 0x1163e , 324 ), # Modi
	( 0x1163f , 0x11640 , 324 ), # Modi
	( 0x11641 , 0x11643 , 324 ), # Modi
	( 0x11644 , 0x11644 , 324 ), # Modi
	( 0x11650 , 0x11659 , 324 ), # Modi
	( 0x11680 , 0x116aa , 321 ), # Takri
	( 0x116ab , 0x116ab , 321 ), # Takri
	( 0x116ac , 0x116ac , 321 ), # Takri
	( 0x116ad , 0x116ad , 321 ), # Takri
	( 0x116ae , 0x116af , 321 ), # Takri
	( 0x116b0 , 0x116b5 , 321 ), # Takri
	( 0x116b6 , 0x116b6 , 321 ), # Takri
	( 0x116b7 , 0x116b7 , 321 ), # Takri
	( 0x116c0 , 0x116c9 , 321 ), # Takri
	( 0x118a0 , 0x118df , 262 ), # Warang_Citi
	( 0x118e0 , 0x118e9 , 262 ), # Warang_Citi
	( 0x118ea , 0x118f2 , 262 ), # Warang_Citi
	( 0x118ff , 0x118ff , 262 ), # Warang_Citi
	( 0x11ac0 , 0x11af8 , 263 ), # Pau_Cin_Hau
	( 0x12000 , 0x12398 , 20 ), # Cuneiform
	( 0x12400 , 0x1246e , 20 ), # Cuneiform
	( 0x12470 , 0x12474 , 20 ), # Cuneiform
	( 0x13000 , 0x1342e , 50 ), # Egyptian_Hieroglyphs
	( 0x16800 , 0x16a38 , 435 ), # Bamum
	( 0x16a40 , 0x16a5e , 199 ), # Mro
	( 0x16a60 , 0x16a69 , 199 ), # Mro
	( 0x16a6e , 0x16a6f , 199 ), # Mro
	( 0x16ad0 , 0x16aed , 259 ), # Bassa_Vah
	( 0x16af0 , 0x16af4 , 259 ), # Bassa_Vah
	( 0x16af5 , 0x16af5 , 259 ), # Bassa_Vah
	( 0x16b00 , 0x16b2f , 450 ), # Pahawh_Hmong
	( 0x16b30 , 0x16b36 , 450 ), # Pahawh_Hmong
	( 0x16b37 , 0x16b3b , 450 ), # Pahawh_Hmong
	( 0x16b3c , 0x16b3f , 450 ), # Pahawh_Hmong
	( 0x16b40 , 0x16b43 , 450 ), # Pahawh_Hmong
	( 0x16b44 , 0x16b44 , 450 ), # Pahawh_Hmong
	( 0x16b45 , 0x16b45 , 450 ), # Pahawh_Hmong
	( 0x16b50 , 0x16b59 , 450 ), # Pahawh_Hmong
	( 0x16b5b , 0x16b61 , 450 ), # Pahawh_Hmong
	( 0x16b63 , 0x16b77 , 450 ), # Pahawh_Hmong
	( 0x16b7d , 0x16b8f , 450 ), # Pahawh_Hmong
	( 0x16f00 , 0x16f44 , 282 ), # Miao
	( 0x16f50 , 0x16f50 , 282 ), # Miao
	( 0x16f51 , 0x16f7e , 282 ), # Miao
	( 0x16f8f , 0x16f92 , 282 ), # Miao
	( 0x16f93 , 0x16f9f , 282 ), # Miao
	( 0x1b000 , 0x1b000 , 411 ), # Katakana
	( 0x1b001 , 0x1b001 , 410 ), # Hiragana
	( 0x1bc00 , 0x1bc6a , 755 ), # Duployan
	( 0x1bc70 , 0x1bc7c , 755 ), # Duployan
	( 0x1bc80 , 0x1bc88 , 755 ), # Duployan
	( 0x1bc90 , 0x1bc99 , 755 ), # Duployan
	( 0x1bc9c , 0x1bc9c , 755 ), # Duployan
	( 0x1bc9d , 0x1bc9e , 755 ), # Duployan
	( 0x1bc9f , 0x1bc9f , 755 ), # Duployan
	( 0x1bca0 , 0x1bca3 , 998 ), # Common
	( 0x1d000 , 0x1d0f5 , 998 ), # Common
	( 0x1d100 , 0x1d126 , 998 ), # Common
	( 0x1d129 , 0x1d164 , 998 ), # Common
	( 0x1d165 , 0x1d166 , 998 ), # Common
	( 0x1d167 , 0x1d169 , 994 ), # Inherited
	( 0x1d16a , 0x1d16c , 998 ), # Common
	( 0x1d16d , 0x1d172 , 998 ), # Common
	( 0x1d173 , 0x1d17a , 998 ), # Common
	( 0x1d17b , 0x1d182 , 994 ), # Inherited
	( 0x1d183 , 0x1d184 , 998 ), # Common
	( 0x1d185 , 0x1d18b , 994 ), # Inherited
	( 0x1d18c , 0x1d1a9 , 998 ), # Common
	( 0x1d1aa , 0x1d1ad , 994 ), # Inherited
	( 0x1d1ae , 0x1d1dd , 998 ), # Common
	( 0x1d200 , 0x1d241 , 200 ), # Greek
	( 0x1d242 , 0x1d244 , 200 ), # Greek
	( 0x1d245 , 0x1d245 , 200 ), # Greek
	( 0x1d300 , 0x1d356 , 998 ), # Common
	( 0x1d360 , 0x1d371 , 998 ), # Common
	( 0x1d400 , 0x1d454 , 998 ), # Common
	( 0x1d456 , 0x1d49c , 998 ), # Common
	( 0x1d49e , 0x1d49f , 998 ), # Common
	( 0x1d4a2 , 0x1d4a2 , 998 ), # Common
	( 0x1d4a5 , 0x1d4a6 , 998 ), # Common
	( 0x1d4a9 , 0x1d4ac , 998 ), # Common
	( 0x1d4ae , 0x1d4b9 , 998 ), # Common
	( 0x1d4bb , 0x1d4bb , 998 ), # Common
	( 0x1d4bd , 0x1d4c3 , 998 ), # Common
	( 0x1d4c5 , 0x1d505 , 998 ), # Common
	( 0x1d507 , 0x1d50a , 998 ), # Common
	( 0x1d50d , 0x1d514 , 998 ), # Common
	( 0x1d516 , 0x1d51c , 998 ), # Common
	( 0x1d51e , 0x1d539 , 998 ), # Common
	( 0x1d53b , 0x1d53e , 998 ), # Common
	( 0x1d540 , 0x1d544 , 998 ), # Common
	( 0x1d546 , 0x1d546 , 998 ), # Common
	( 0x1d54a , 0x1d550 , 998 ), # Common
	( 0x1d552 , 0x1d6a5 , 998 ), # Common
	( 0x1d6a8 , 0x1d6c0 , 998 ), # Common
	( 0x1d6c1 , 0x1d6c1 , 998 ), # Common
	( 0x1d6c2 , 0x1d6da , 998 ), # Common
	( 0x1d6db , 0x1d6db , 998 ), # Common
	( 0x1d6dc , 0x1d6fa , 998 ), # Common
	( 0x1d6fb , 0x1d6fb , 998 ), # Common
	( 0x1d6fc , 0x1d714 , 998 ), # Common
	( 0x1d715 , 0x1d715 , 998 ), # Common
	( 0x1d716 , 0x1d734 , 998 ), # Common
	( 0x1d735 , 0x1d735 , 998 ), # Common
	( 0x1d736 , 0x1d74e , 998 ), # Common
	( 0x1d74f , 0x1d74f , 998 ), # Common
	( 0x1d750 , 0x1d76e , 998 ), # Common
	( 0x1d76f , 0x1d76f , 998 ), # Common
	( 0x1d770 , 0x1d788 , 998 ), # Common
	( 0x1d789 , 0x1d789 , 998 ), # Common
	( 0x1d78a , 0x1d7a8 , 998 ), # Common
	( 0x1d7a9 , 0x1d7a9 , 998 ), # Common
	( 0x1d7aa , 0x1d7c2 , 998 ), # Common
	( 0x1d7c3 , 0x1d7c3 , 998 ), # Common
	( 0x1d7c4 , 0x1d7cb , 998 ), # Common
	( 0x1d7ce , 0x1d7ff , 998 ), # Common
	( 0x1e800 , 0x1e8c4 , 438 ), # Mende_Kikakui
	( 0x1e8c7 , 0x1e8cf , 438 ), # Mende_Kikakui
	( 0x1e8d0 , 0x1e8d6 , 438 ), # Mende_Kikakui
	( 0x1ee00 , 0x1ee03 , 160 ), # Arabic
	( 0x1ee05 , 0x1ee1f , 160 ), # Arabic
	( 0x1ee21 , 0x1ee22 , 160 ), # Arabic
	( 0x1ee24 , 0x1ee24 , 160 ), # Arabic
	( 0x1ee27 , 0x1ee27 , 160 ), # Arabic
	( 0x1ee29 , 0x1ee32 , 160 ), # Arabic
	( 0x1ee34 , 0x1ee37 , 160 ), # Arabic
	( 0x1ee39 , 0x1ee39 , 160 ), # Arabic
	( 0x1ee3b , 0x1ee3b , 160 ), # Arabic
	( 0x1ee42 , 0x1ee42 , 160 ), # Arabic
	( 0x1ee47 , 0x1ee47 , 160 ), # Arabic
	( 0x1ee49 , 0x1ee49 , 160 ), # Arabic
	( 0x1ee4b , 0x1ee4b , 160 ), # Arabic
	( 0x1ee4d , 0x1ee4f , 160 ), # Arabic
	( 0x1ee51 , 0x1ee52 , 160 ), # Arabic
	( 0x1ee54 , 0x1ee54 , 160 ), # Arabic
	( 0x1ee57 , 0x1ee57 , 160 ), # Arabic
	( 0x1ee59 , 0x1ee59 , 160 ), # Arabic
	( 0x1ee5b , 0x1ee5b , 160 ), # Arabic
	( 0x1ee5d , 0x1ee5d , 160 ), # Arabic
	( 0x1ee5f , 0x1ee5f , 160 ), # Arabic
	( 0x1ee61 , 0x1ee62 , 160 ), # Arabic
	( 0x1ee64 , 0x1ee64 , 160 ), # Arabic
	( 0x1ee67 , 0x1ee6a , 160 ), # Arabic
	( 0x1ee6c , 0x1ee72 , 160 ), # Arabic
	( 0x1ee74 , 0x1ee77 , 160 ), # Arabic
	( 0x1ee79 , 0x1ee7c , 160 ), # Arabic
	( 0x1ee7e , 0x1ee7e , 160 ), # Arabic
	( 0x1ee80 , 0x1ee89 , 160 ), # Arabic
	( 0x1ee8b , 0x1ee9b , 160 ), # Arabic
	( 0x1eea1 , 0x1eea3 , 160 ), # Arabic
	( 0x1eea5 , 0x1eea9 , 160 ), # Arabic
	( 0x1eeab , 0x1eebb , 160 ), # Arabic
	( 0x1eef0 , 0x1eef1 , 160 ), # Arabic
	( 0x1f000 , 0x1f02b , 998 ), # Common
	( 0x1f030 , 0x1f093 , 998 ), # Common
	( 0x1f0a0 , 0x1f0ae , 998 ), # Common
	( 0x1f0b1 , 0x1f0bf , 998 ), # Common
	( 0x1f0c1 , 0x1f0cf , 998 ), # Common
	( 0x1f0d1 , 0x1f0f5 , 998 ), # Common
	( 0x1f100 , 0x1f10c , 998 ), # Common
	( 0x1f110 , 0x1f12e , 998 ), # Common
	( 0x1f130 , 0x1f16b , 998 ), # Common
	( 0x1f170 , 0x1f19a , 998 ), # Common
	( 0x1f1e6 , 0x1f1ff , 998 ), # Common
	( 0x1f200 , 0x1f200 , 410 ), # Hiragana
	( 0x1f201 , 0x1f202 , 998 ), # Common
	( 0x1f210 , 0x1f23a , 998 ), # Common
	( 0x1f240 , 0x1f248 , 998 ), # Common
	( 0x1f250 , 0x1f251 , 998 ), # Common
	( 0x1f300 , 0x1f32c , 998 ), # Common
	( 0x1f330 , 0x1f37d , 998 ), # Common
	( 0x1f380 , 0x1f3ce , 998 ), # Common
	( 0x1f3d4 , 0x1f3f7 , 998 ), # Common
	( 0x1f400 , 0x1f4fe , 998 ), # Common
	( 0x1f500 , 0x1f54a , 998 ), # Common
	( 0x1f550 , 0x1f579 , 998 ), # Common
	( 0x1f57b , 0x1f5a3 , 998 ), # Common
	( 0x1f5a5 , 0x1f642 , 998 ), # Common
	( 0x1f645 , 0x1f6cf , 998 ), # Common
	( 0x1f6e0 , 0x1f6ec , 998 ), # Common
	( 0x1f6f0 , 0x1f6f3 , 998 ), # Common
	( 0x1f700 , 0x1f773 , 998 ), # Common
	( 0x1f780 , 0x1f7d4 , 998 ), # Common
	( 0x1f800 , 0x1f80b , 998 ), # Common
	( 0x1f810 , 0x1f847 , 998 ), # Common
	( 0x1f850 , 0x1f859 , 998 ), # Common
	( 0x1f860 , 0x1f887 , 998 ), # Common
	( 0x1f890 , 0x1f8ad , 998 ), # Common
	( 0x20000 , 0x2a6d6 , 500 ), # Han
	( 0x2a700 , 0x2b734 , 500 ), # Han
	( 0x2b740 , 0x2b81d , 500 ), # Han
	( 0x2f800 , 0x2fa1d , 500 ), # Han
	( 0xe0001 , 0xe0001 , 998 ), # Common
	( 0xe0020 , 0xe007f , 998 ), # Common
	( 0xe0100 , 0xe01ef , 994 ), # Inherited
]

unicodeScriptNamesToISO15924Dictionary = {
	"Caucasian_Albanian":239, 
	"Arabic":160,
	"Imperial_Aramaic":124, 
	"Armenian":230,
	"Avestan":134,
	"Balinese":360,
	"Bamum":435,
	"Bassa_Vah":259,
	"Batak":365,
	"Bengali":325,
	"Bopomofo":285,
	"Brahmi":300,
	"Braille":570,
	"Buginese":367,
	"Buhid":372,
	"Chakma":349,
	"Canadian_Aboriginal":440,
	"Carian":201,
	"Cham":358,
	"Cherokee":445,
	"Coptic":204,
	"Cypriot":403,
	"Cyrillic":220,
	"Devanagari":315,
	"Deseret":250,
	"Duployan":755,
	"Egyptian_Hieroglyphs":50,
	"Elbasan":226,
	"Ethiopic":430,
	"Georgian":240,
	"Glagolitic":225,
	"Gothic":206,
	"Grantha":343,
	"Greek":200,
	"Gujarati":320,
	"Gurmukhi":310,
	"Hangul":286,
	"Han":500,
	"Hanunoo":371,
	"Hebrew":125,
	"Hiragana":410,
	"Pahawh_Hmong":450,
	"Old_Italic":210,
	"Javanese":361,
	"Kayah_Li":357,
	"Katakana":411,
	"Kharoshthi":305,
	"Khmer":355,
	"Khojki":322,
	"Kannada":345,
	"Kaithi":317,
	"Lao":356,
	"Latin":215,
	"Lepcha":335,
	"Limbu":336,
	"Linear_A":400,
	"Linear_B":401,
	"Lisu":399,
	"Lycian":202,
	"Lydian":116,
	"Mahajani":314,
	"Mandaic":140,
	"Manichaean":139,
	"Mende_Kikakui":438,
	"Meroitic_Cursive":101,
	"Meroitic_Hieroglyphs":100,
	"Malayalam":347,
	"Modi":324,
	"Mongolian":145,
	"Mro":199,
	"Meetei_Mayek":337,
	"Multani":323,
	"Myanmar":350,
	"Old_North_Arabian":106,
	"Nabataean":159,
	"Nko":165,
	"Ogham":212,
	"Ol_Chiki":261,
	"Old_Turkic":175,
	"Oriya":327,
	"Osage":219,
	"Osmanya":260,
	"Palmyrene":126,
	"Pau_Cin_Hau":263,
	"Old_Permic":227,
	"Phags_Pa":331,
	"Inscriptional_Pahlavi":131,
	"Psalter_Pahlavi":132,
	"Book_Pahlavi":133,
	"Phoenician":115,
	"Miao":282,
	"Inscriptional_Parthian":130,
	"Rejang":363,
	"Rongorongo":620,
	"Runic":211,
	"Samaritan":123,
	"Sarati":292,
	"Old_South_Arabian":105,
	"Saurashtra":344,
	"Shavian":281,
	"Sharada":319,
	"Siddham":302,
	"Khudawadi":318,
	"Sinhala":348,
	"Sora_Sompeng":398,
	"Sundanese":362,
	"Syloti_Nagri":316,
	"Syriac":135,
	"Tagbanwa":373,
	"Takri":321,
	"Tai_Le":353,
	"New_Tai_Lue":354,
	"Tamil":346,
	"Tangut":520,
	"Tai_Viet":359,
	"Telugu":340,
	"Tengwar":290,
	"Tifinagh":120,
	"Tagalog":370,
	"Thaana":170,
	"Thai":352,
	"Tibetan":330,
	"Tirhuta":326,
	"Ugaritic":40,
	"Vai":470,
	"Warang_Citi":262,
	"Woleai":480,
	"Old_Persian":30,
	"Cuneiform":20,
	"Yi":460,
	"Inherited":994,
	"Symbols":996,
	"Common":998,
	"Unknown":999,
}

ISO15924ToUnicodeScriptNamesDictionary = {}

langIDToScriptID= {
	'af_ZA':215, # south african
	'am':230, # Armenian 
	'ar':160, # Arabic 
	'as':325 , # Assamese 
	'bg':220, # Bulgarian 
	'bn':325, # Bangla 
	'ca':215, # Catalan 
	'cs':215, # Czech 
	'da':215, # Danish 
	'de':215, # German 
	'el':215, # Greek 
	'en':215, # english
	'es':215, # spanish
	'gu':320, # Gujarati 
	'hi':315, # Hindi (hi)
	'kn':345, # kanada
	'ml':347, # Malayalam 
	'mn':145, # mongolian
	'mr':315, # Marathi (mr),
	'ne':315, # Nepali (ne),
	'or':327, # Oriya
	'pa':310, # Punjabi
	'sa':315, # Sanskrit (sa)
	'sq':239, # Albanian 
	'ta':346, # Tamil
	'te':340, # Telugu 
}

scriptIDToLangID = {
	239:'sq', # 0x041C,   # Caucasian_Albanian:Albanian (sq) 
	160:'ar', # 0x1401, # "Arabic":Arabic (ar)
	# "Imperial_Aramaic":124, 
	230:'am', # 0x042B, # "Armenian":Armenian (hy)
	#"Avestan":134,
	#"Balinese":360,
	#"Bamum":435,
	#"Bassa_Vah":259,
	#"Batak":365,
	325:('bn','as'), # (0x0445,0x044D), # "Bengali":Bangla (bn),Assamese (as)
	#"Bopomofo":285,
	#"Brahmi":300,
	#"Braille":570,
	#"Buginese":367,
	#"Buhid":372,
	#"Chakma":349,
	#"Canadian_Aboriginal":440,
	#"Carian":201,
	#"Cham":358,
	#"Cherokee":445,
	#"Coptic":204,
	#"Cypriot":403,
	220:'bg', # (0x0402), # "Cyrillic":Bulgarian (bg)
	315:('hi','mr','ne','sa'), # (0x0439,0x044E,0x0461,0x044F), # "Devanagari":Hindi (hi),Marathi (mr),Nepali (ne),Sanskrit (sa)
	#"Deseret":250,
	#"Duployan":755,
	#"Egyptian_Hieroglyphs":50,
	#"Elbasan":226,
	#"Ethiopic":430,
	#"Georgian":240,
	#"Glagolitic":225,
	#"Gothic":206,
	#"Grantha":343,
	#"Greek":200,
	320:'gu', # 0x0447, # "Gujarati":Gujarati (gu)
	310:'pa', # 0x0446, # "Gurmukhi":Punjabi (pa)
	#"Hangul":286,
	#"Han":500,
	#"Hanunoo":371,
	#"Hebrew":125,
	#"Hiragana":410,
	#"Pahawh_Hmong":450,
	#"Old_Italic":210,
	#"Javanese":361,
	#"Kayah_Li":357,
	#"Katakana":411,
	#"Kharoshthi":305,
	#"Khmer":355,
	#"Khojki":322,
	345:'kn', # 0x044B, # "Kannada":Kannada (kn)
	#"Kaithi":317,
	#"Lao":356,
	215:('e','af_ZA','ca','cs','da','de','el','es'), # 0x0409, # "Latin":English (en)
	#"Lepcha":335,
	#"Limbu":336,
	#"Linear_A":400,
	#"Linear_B":401,
	#"Lisu":399,
	#"Lycian":202,
	#"Lydian":116,
	#"Mahajani":314,
	#"Mandaic":140,
	#"Manichaean":139,
	#"Mende_Kikakui":438,
	#"Meroitic_Cursive":101,
	#"Meroitic_Hieroglyphs":100,
	347:'ml', # 0x044C, # "Malayalam":Malayalam (ml)
	#"Modi":324,
	145:'mn', # 0x0450 , # "Mongolian":Mongolian (mn)
	#"Mro":199,
	#"Meetei_Mayek":337,
	#"Multani":323,
	#"Myanmar":350,
	#"Old_North_Arabian":106,
	#"Nabataean":159,
	#"Nko":165,
	#"Ogham":212,
	#"Ol_Chiki":261,
	#"Old_Turkic":175,
	327:'or', # 0x0448, # "Oriya":Oriya (or)
	#"Osage":219,
	#"Osmanya":260,
	#"Palmyrene":126,
	#"Pau_Cin_Hau":263,
	#"Old_Permic":227,
	#"Phags_Pa":331,
	#"Inscriptional_Pahlavi":131,
	#"Psalter_Pahlavi":132,
	#"Book_Pahlavi":133,
	#"Phoenician":115,
	#"Miao":282,
	#"Inscriptional_Parthian":130,
	#"Rejang":363,
	#"Rongorongo":620,
	#"Runic":211,
	#"Samaritan":123,
	#"Sarati":292,
	#"Old_South_Arabian":105,
	#"Saurashtra":344,
	#"Shavian":281,
	#"Sharada":319,
	#"Siddham":302,
	#"Khudawadi":318,
	#"Sinhala":348,
	#"Sora_Sompeng":398,
	#"Sundanese":362,
	#"Syloti_Nagri":316,
	#"Syriac":135,
	#"Tagbanwa":373,
	#"Takri":321,
	#"Tai_Le":353,
	#"New_Tai_Lue":354,
	346:'ta', # 0x0449, # "Tamil":Tamil (ta)
	#"Tangut":520,
	#"Tai_Viet":359,
	340:'te', # 0x044A, # "Telugu":Telugu (te)
	#"Tengwar":290,
	#"Tifinagh":120,
	#"Tagalog":370,
	#"Thaana":170,
	#"Thai":352,
	#"Tibetan":330,
	#"Tirhuta":326,
	#"Ugaritic":40,
	#"Vai":470,
	#"Warang_Citi":262,
	#"Woleai":480,
	#"Old_Persian":30,
	#"Cuneiform":20,
	#"Yi":460,
	#"Inherited":994,
	#"Symbols":996,
	#"Common":998,
	#"Unknown":999,
}

languagePriorityListSpec = []

def initialize():
	# initializing reverse dictionary ISO15924ToUnicodeScriptNamesDictionary
	for scriptName in unicodeScriptNamesToISO15924Dictionary.keys():
		ISO15924ToUnicodeScriptNamesDictionary.setdefault( unicodeScriptNamesToISO15924Dictionary[scriptName] , scriptName )
	#reading string from config and convert it to list
	languageList = config.conf["writingScriptsToLanguage"]["languagePriorityList"].split(",")
	for language in languageList: 
		languagePriorityListSpec.append( [ language , getScriptName(language) , getLanguageDescription( language ) ]) 

def getAvailableLanguages():
	"""generates a list of locale names, plus their full localized language and country names.
	@rtype: list of tuples
	"""
	#Make a list of all the locales found in NVDA's locale dir
	allLanguages  = langIDToScriptID.keys()
	allLanguages.sort()
	languageCodes = [] 
	languageDescriptions = []
	for language in allLanguages:  
		if language in [j for i in languagePriorityListSpec for j in i]:
			continue
		else:
			languageCodes.append(language )
			desc=languageHandler.getLanguageDescription(language )
			label="%s, %s"%(desc,language ) if desc else language 
			languageDescriptions.append(label)
	return zip(languageCodes , languageDescriptions)



def getScriptCode(chr):
	mStart = 0
	mEnd = len(scriptCode)-1
	characterUnicodeCode = ord(chr)
	while( mEnd >= mStart ):
		midPoint = (mStart + mEnd ) >> 1
		if characterUnicodeCode < scriptCode[midPoint][0]: 
			mEnd = midPoint -1
		elif characterUnicodeCode > scriptCode[midPoint][1]: 
			mStart = midPoint + 1
		else:
			return scriptCode[midPoint][2] 
	return 0

def getLangID(scriptCode):
	scriptName = ISO15924ToUnicodeScriptNamesDictionary[ scriptCode ] 
	for index in xrange( len( languagePriorityListSpec) ) :
		if scriptName == languagePriorityListSpec[index][1]: 
			return languagePriorityListSpec[index][0] 
	#language not found in the priority list, so look up in the default mapping
	langID = scriptIDToLangID.get (scriptCode )
	if langID:
		if isinstance( langID , tuple) and len(langID) > 0:
			return langID[0]
		else:
			return langID

def getLanguageDescription(language ):
	desc=languageHandler.getLanguageDescription(language )
	label="%s, %s"%(desc,language ) if desc else language 
	return label

def getScriptIDFromLangID(langID ):
	scriptID = langIDToScriptID.get (langID )
	if scriptID: 
		if isinstance( scriptID , tuple) and len(langID) > 0:
			return scriptID [0]
		else:
			return scriptID 


def getScriptName(languageID ):
	scriptID = getScriptIDFromLangID( languageID )
	if scriptID:
		return ISO15924ToUnicodeScriptNamesDictionary[ scriptID ]  


def detectScript(text):
	unicodeSequence = []
	currentScript = getScriptCode(  text[0])
	oldScript = currentScript
	unicodeSequence.append(LangChangeCommand(currentScript)) 
	beginIndex = 0
	for index in xrange( len(text) ) :
		currentScript = getScriptCode( text[index] ) 
		if currentScript == 998: 
			continue

		if currentScript != oldScript:
			newText = text[beginIndex:index] 
			unicodeSequence.append( newText )
			beginIndex= index
			unicodeSequence.append(LangChangeCommand(currentScript)) 
		oldScript = currentScript

	unicodeSequence.append( text[beginIndex:] )
	return unicodeSequence

def detectLanguage(text):
	sequenceWithScript = detectScript(text)

	for index in xrange(len(sequenceWithScript )):
		item= sequenceWithScript [index]
		if isinstance(item,LangChangeCommand):
			sequenceWithScript [index] = LangChangeCommand( languageHandler.normalizeLanguage( getLangID( item.lang )  ) )
	return sequenceWithScript 


#detectScript("dinesh@kaushal\u0915hint".decode('unicode_escape')  )

def _compile_scripts_txt():
    # build indexes from 'scripts.txt'

	unicodeRange= []



	import urllib2, re, textwrap

	url = 'http://www.unicode.org/Public/UNIDATA/Scripts.txt'
	f = urllib2.urlopen(url)
	for ln in f:
		p = re.findall(r'([0-9A-F]+)(?:\.\.([0-9A-F]+))?\W+(\w+)\s*#\s*(\w+)', ln)
		if p:
			a, b, name, cat = p[0]
			if name in unicodeScriptNamesToISO15924Dictionary.keys():
				tempScriptCode = unicodeScriptNamesToISO15924Dictionary[name]
				unicodeRange.append((int(a, 16), int(b or a, 16), tempScriptCode , name ))
	unicodeRange.sort()



	print 'scriptCode= [\n%s\n]' % (
		'\n'.join('\t( 0x%x , 0x%x , %d ), # %s' % c for c in unicodeRange) )        

#profile.run("for i in range(0,100000): getScriptIDFromLangID('en')")


#print "script {}".format( getScriptIDFromLangID('hi'))
#print "langID: {}".format(getLangID(215))