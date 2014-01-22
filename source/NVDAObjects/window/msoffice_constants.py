# office_constants.py
# Usage : from office_constants import *
# xlFooBar.get( an_integer )
# returns text to be spoken
# Translators: full of small phrases. 


class xlConstant(object):
	@classmethod
	def get(cls,x):
		try:
			return cls._map[x]
		except:
			return str(x)

class xlBordersIndex(xlConstant):
	xlDiagonalDown                =5
	xlDiagonalUp                  =6
	xlEdgeBottom                  =9
	xlEdgeLeft                    =7
	xlEdgeRight                   =10
	xlEdgeTop                     =8
	xlInsideHorizontal            =12
	xlInsideVertical              =11
	_map = {
		xlDiagonalDown                :_("diagonal down"),
		xlDiagonalUp                  :_("diagonal up"),
		xlEdgeBottom                  :_("edge bottom"),
		xlEdgeLeft                    :_("edge left"),
		xlEdgeRight                   :_("edge right"),
		xlEdgeTop                     :_("edge top"),
		xlInsideHorizontal            :_("inside horizontal"),
		xlInsideVertical              :_("inside vertical"),
	}
	_list = [ xlEdgeBottom, xlEdgeLeft, xlEdgeRight,xlEdgeTop ]

class xlHAlign(xlConstant):
	xlHAlignCenter                =-4108
	xlHAlignCenterAcrossSelection =7
	xlHAlignDistributed           =-4117
	xlHAlignFill                  =5
	xlHAlignGeneral               =1
	xlHAlignJustify               =-4130
	xlHAlignLeft                  =-4131
	xlHAlignRight                 =-4152

	_map = {
		xlHAlignCenter                :_("center"),
		xlHAlignCenterAcrossSelection :_("center across selection"),
		xlHAlignDistributed           :_("distributed"),
		xlHAlignFill                  :_("fill"),
		xlHAlignGeneral               :_("general"),
		xlHAlignJustify               :_("justify "),
		xlHAlignLeft                  :_("left"),
		xlHAlignRight                 :_("right "),
	}

class xlVAlign(xlConstant):
	xlVAlignBottom                =-4107
	xlVAlignCenter                =-4108
	xlVAlignDistributed           =-4117
	xlVAlignJustify               =-4130
	xlVAlignTop                   =-4160

	_map = {
		xlVAlignBottom                :_("bottom"),
		xlVAlignCenter                :_("center"),
		xlVAlignDistributed           :_("distributed"),
		xlVAlignJustify               :_("justify"),
		xlVAlignTop                   :_("top"),
	}

class xlBordersWeight(xlConstant):
	xlHairline                    =1
	xlMedium                      =-4138
	xlThick                       =4
	xlThin                        =2
	_map = {
		xlHairline                    :_("hair line"),
		xlMedium                      :_("medium "),
		xlThick                       :_("thick"),
		xlThin                        :_("thin"),
	}
	
class xlLineStyle(xlConstant):
	xlContinuous                  =1
	xlDash                        =-4115
	xlDashDot                     =4
	xlDashDotDot                  =5
	xlDot                         =-4118
	xlDouble                      =-4119
	xlLineStyleNone               =-4142
	xlSlantDashDot                =13

	_map = {
		xlContinuous                  :_("continous"),
		xlDash                        :_("dash"),
		xlDashDot                     :_("dash dot"),
		xlDashDotDot                  :_("dash dot dot"),
		xlDot                         :_("dot"),
		xlDouble                      :_("double"),
		xlLineStyleNone               :_("none"),
		xlSlantDashDot                :_("slant dash dot"),
	}
	
class xlCellType(xlConstant):
	xlCellTypeAllFormatConditions =-4172      # from enum XlCellType
	xlCellTypeAllValidation       =-4174      # from enum XlCellType
	xlCellTypeBlanks              =4          # from enum XlCellType
	xlCellTypeComments            =-4144      # from enum XlCellType
	xlCellTypeConstants           =2          # from enum XlCellType
	xlCellTypeFormulas            =-4123      # from enum XlCellType
	xlCellTypeLastCell            =11         # from enum XlCellType
	xlCellTypeSameFormatConditions=-4173      # from enum XlCellType
	xlCellTypeSameValidation      =-4175      # from enum XlCellType
	xlCellTypeVisible             =12         # from enum XlCellType

        ## These are actually from xlSpecialCellsValue
	xlErrors                      = 16
	xlLogical                     = 4
	xlNumbers                     = 1
	xlTextValues                  = 2

	_map = { 
		xlCellTypeAllFormatConditions :_("any format"),
		xlCellTypeAllValidation       :_("validatio"),
		xlCellTypeBlanks              :_("empty cell"),
		xlCellTypeComments            :_("comment"),
		xlCellTypeConstants           :_("constant"),
		xlCellTypeFormulas            :_("formula"),
		xlCellTypeLastCell            :_("last cell"),
		xlCellTypeSameFormatConditions:_("same format conditions"),
		xlCellTypeSameValidation      :_("same validation"),
		xlCellTypeVisible             :_("visible"),
	}
