# Generated from Python2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Python2Parser import Python2Parser
else:
    from Python2Parser import Python2Parser

# This class defines a complete listener for a parse tree produced by Python2Parser.
class Python2Listener(ParseTreeListener):

    # Enter a parse tree produced by Python2Parser#single_input.
    def enterSingle_input(self, ctx:Python2Parser.Single_inputContext):
        pass

    # Exit a parse tree produced by Python2Parser#single_input.
    def exitSingle_input(self, ctx:Python2Parser.Single_inputContext):
        pass


    # Enter a parse tree produced by Python2Parser#file_input.
    def enterFile_input(self, ctx:Python2Parser.File_inputContext):
        pass

    # Exit a parse tree produced by Python2Parser#file_input.
    def exitFile_input(self, ctx:Python2Parser.File_inputContext):
        pass


    # Enter a parse tree produced by Python2Parser#eval_input.
    def enterEval_input(self, ctx:Python2Parser.Eval_inputContext):
        pass

    # Exit a parse tree produced by Python2Parser#eval_input.
    def exitEval_input(self, ctx:Python2Parser.Eval_inputContext):
        pass


    # Enter a parse tree produced by Python2Parser#decorator.
    def enterDecorator(self, ctx:Python2Parser.DecoratorContext):
        pass

    # Exit a parse tree produced by Python2Parser#decorator.
    def exitDecorator(self, ctx:Python2Parser.DecoratorContext):
        pass


    # Enter a parse tree produced by Python2Parser#decorators.
    def enterDecorators(self, ctx:Python2Parser.DecoratorsContext):
        pass

    # Exit a parse tree produced by Python2Parser#decorators.
    def exitDecorators(self, ctx:Python2Parser.DecoratorsContext):
        pass


    # Enter a parse tree produced by Python2Parser#decorated.
    def enterDecorated(self, ctx:Python2Parser.DecoratedContext):
        pass

    # Exit a parse tree produced by Python2Parser#decorated.
    def exitDecorated(self, ctx:Python2Parser.DecoratedContext):
        pass


    # Enter a parse tree produced by Python2Parser#funcdef.
    def enterFuncdef(self, ctx:Python2Parser.FuncdefContext):
        pass

    # Exit a parse tree produced by Python2Parser#funcdef.
    def exitFuncdef(self, ctx:Python2Parser.FuncdefContext):
        pass


    # Enter a parse tree produced by Python2Parser#parameters.
    def enterParameters(self, ctx:Python2Parser.ParametersContext):
        pass

    # Exit a parse tree produced by Python2Parser#parameters.
    def exitParameters(self, ctx:Python2Parser.ParametersContext):
        pass


    # Enter a parse tree produced by Python2Parser#varargslist.
    def enterVarargslist(self, ctx:Python2Parser.VarargslistContext):
        pass

    # Exit a parse tree produced by Python2Parser#varargslist.
    def exitVarargslist(self, ctx:Python2Parser.VarargslistContext):
        pass


    # Enter a parse tree produced by Python2Parser#fpdef.
    def enterFpdef(self, ctx:Python2Parser.FpdefContext):
        pass

    # Exit a parse tree produced by Python2Parser#fpdef.
    def exitFpdef(self, ctx:Python2Parser.FpdefContext):
        pass


    # Enter a parse tree produced by Python2Parser#fplist.
    def enterFplist(self, ctx:Python2Parser.FplistContext):
        pass

    # Exit a parse tree produced by Python2Parser#fplist.
    def exitFplist(self, ctx:Python2Parser.FplistContext):
        pass


    # Enter a parse tree produced by Python2Parser#stmt.
    def enterStmt(self, ctx:Python2Parser.StmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#stmt.
    def exitStmt(self, ctx:Python2Parser.StmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#simple_stmt.
    def enterSimple_stmt(self, ctx:Python2Parser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#simple_stmt.
    def exitSimple_stmt(self, ctx:Python2Parser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#small_stmt.
    def enterSmall_stmt(self, ctx:Python2Parser.Small_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#small_stmt.
    def exitSmall_stmt(self, ctx:Python2Parser.Small_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#expr_stmt.
    def enterExpr_stmt(self, ctx:Python2Parser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#expr_stmt.
    def exitExpr_stmt(self, ctx:Python2Parser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#augassign.
    def enterAugassign(self, ctx:Python2Parser.AugassignContext):
        pass

    # Exit a parse tree produced by Python2Parser#augassign.
    def exitAugassign(self, ctx:Python2Parser.AugassignContext):
        pass


    # Enter a parse tree produced by Python2Parser#print_stmt.
    def enterPrint_stmt(self, ctx:Python2Parser.Print_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#print_stmt.
    def exitPrint_stmt(self, ctx:Python2Parser.Print_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#del_stmt.
    def enterDel_stmt(self, ctx:Python2Parser.Del_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#del_stmt.
    def exitDel_stmt(self, ctx:Python2Parser.Del_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#pass_stmt.
    def enterPass_stmt(self, ctx:Python2Parser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#pass_stmt.
    def exitPass_stmt(self, ctx:Python2Parser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#flow_stmt.
    def enterFlow_stmt(self, ctx:Python2Parser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#flow_stmt.
    def exitFlow_stmt(self, ctx:Python2Parser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#break_stmt.
    def enterBreak_stmt(self, ctx:Python2Parser.Break_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#break_stmt.
    def exitBreak_stmt(self, ctx:Python2Parser.Break_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#continue_stmt.
    def enterContinue_stmt(self, ctx:Python2Parser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#continue_stmt.
    def exitContinue_stmt(self, ctx:Python2Parser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#return_stmt.
    def enterReturn_stmt(self, ctx:Python2Parser.Return_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#return_stmt.
    def exitReturn_stmt(self, ctx:Python2Parser.Return_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#yield_stmt.
    def enterYield_stmt(self, ctx:Python2Parser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#yield_stmt.
    def exitYield_stmt(self, ctx:Python2Parser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#raise_stmt.
    def enterRaise_stmt(self, ctx:Python2Parser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#raise_stmt.
    def exitRaise_stmt(self, ctx:Python2Parser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#import_stmt.
    def enterImport_stmt(self, ctx:Python2Parser.Import_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#import_stmt.
    def exitImport_stmt(self, ctx:Python2Parser.Import_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#import_name.
    def enterImport_name(self, ctx:Python2Parser.Import_nameContext):
        pass

    # Exit a parse tree produced by Python2Parser#import_name.
    def exitImport_name(self, ctx:Python2Parser.Import_nameContext):
        pass


    # Enter a parse tree produced by Python2Parser#import_from.
    def enterImport_from(self, ctx:Python2Parser.Import_fromContext):
        pass

    # Exit a parse tree produced by Python2Parser#import_from.
    def exitImport_from(self, ctx:Python2Parser.Import_fromContext):
        pass


    # Enter a parse tree produced by Python2Parser#import_as_name.
    def enterImport_as_name(self, ctx:Python2Parser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by Python2Parser#import_as_name.
    def exitImport_as_name(self, ctx:Python2Parser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by Python2Parser#dotted_as_name.
    def enterDotted_as_name(self, ctx:Python2Parser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by Python2Parser#dotted_as_name.
    def exitDotted_as_name(self, ctx:Python2Parser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by Python2Parser#import_as_names.
    def enterImport_as_names(self, ctx:Python2Parser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by Python2Parser#import_as_names.
    def exitImport_as_names(self, ctx:Python2Parser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by Python2Parser#dotted_as_names.
    def enterDotted_as_names(self, ctx:Python2Parser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by Python2Parser#dotted_as_names.
    def exitDotted_as_names(self, ctx:Python2Parser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by Python2Parser#dotted_name.
    def enterDotted_name(self, ctx:Python2Parser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by Python2Parser#dotted_name.
    def exitDotted_name(self, ctx:Python2Parser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by Python2Parser#global_stmt.
    def enterGlobal_stmt(self, ctx:Python2Parser.Global_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#global_stmt.
    def exitGlobal_stmt(self, ctx:Python2Parser.Global_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#exec_stmt.
    def enterExec_stmt(self, ctx:Python2Parser.Exec_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#exec_stmt.
    def exitExec_stmt(self, ctx:Python2Parser.Exec_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#assert_stmt.
    def enterAssert_stmt(self, ctx:Python2Parser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#assert_stmt.
    def exitAssert_stmt(self, ctx:Python2Parser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#compound_stmt.
    def enterCompound_stmt(self, ctx:Python2Parser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#compound_stmt.
    def exitCompound_stmt(self, ctx:Python2Parser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#if_stmt.
    def enterIf_stmt(self, ctx:Python2Parser.If_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#if_stmt.
    def exitIf_stmt(self, ctx:Python2Parser.If_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#while_stmt.
    def enterWhile_stmt(self, ctx:Python2Parser.While_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#while_stmt.
    def exitWhile_stmt(self, ctx:Python2Parser.While_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#for_stmt.
    def enterFor_stmt(self, ctx:Python2Parser.For_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#for_stmt.
    def exitFor_stmt(self, ctx:Python2Parser.For_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#try_stmt.
    def enterTry_stmt(self, ctx:Python2Parser.Try_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#try_stmt.
    def exitTry_stmt(self, ctx:Python2Parser.Try_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#with_stmt.
    def enterWith_stmt(self, ctx:Python2Parser.With_stmtContext):
        pass

    # Exit a parse tree produced by Python2Parser#with_stmt.
    def exitWith_stmt(self, ctx:Python2Parser.With_stmtContext):
        pass


    # Enter a parse tree produced by Python2Parser#with_item.
    def enterWith_item(self, ctx:Python2Parser.With_itemContext):
        pass

    # Exit a parse tree produced by Python2Parser#with_item.
    def exitWith_item(self, ctx:Python2Parser.With_itemContext):
        pass


    # Enter a parse tree produced by Python2Parser#except_clause.
    def enterExcept_clause(self, ctx:Python2Parser.Except_clauseContext):
        pass

    # Exit a parse tree produced by Python2Parser#except_clause.
    def exitExcept_clause(self, ctx:Python2Parser.Except_clauseContext):
        pass


    # Enter a parse tree produced by Python2Parser#suite.
    def enterSuite(self, ctx:Python2Parser.SuiteContext):
        pass

    # Exit a parse tree produced by Python2Parser#suite.
    def exitSuite(self, ctx:Python2Parser.SuiteContext):
        pass


    # Enter a parse tree produced by Python2Parser#testlist_safe.
    def enterTestlist_safe(self, ctx:Python2Parser.Testlist_safeContext):
        pass

    # Exit a parse tree produced by Python2Parser#testlist_safe.
    def exitTestlist_safe(self, ctx:Python2Parser.Testlist_safeContext):
        pass


    # Enter a parse tree produced by Python2Parser#old_test.
    def enterOld_test(self, ctx:Python2Parser.Old_testContext):
        pass

    # Exit a parse tree produced by Python2Parser#old_test.
    def exitOld_test(self, ctx:Python2Parser.Old_testContext):
        pass


    # Enter a parse tree produced by Python2Parser#old_lambdef.
    def enterOld_lambdef(self, ctx:Python2Parser.Old_lambdefContext):
        pass

    # Exit a parse tree produced by Python2Parser#old_lambdef.
    def exitOld_lambdef(self, ctx:Python2Parser.Old_lambdefContext):
        pass


    # Enter a parse tree produced by Python2Parser#test.
    def enterTest(self, ctx:Python2Parser.TestContext):
        pass

    # Exit a parse tree produced by Python2Parser#test.
    def exitTest(self, ctx:Python2Parser.TestContext):
        pass


    # Enter a parse tree produced by Python2Parser#or_test.
    def enterOr_test(self, ctx:Python2Parser.Or_testContext):
        pass

    # Exit a parse tree produced by Python2Parser#or_test.
    def exitOr_test(self, ctx:Python2Parser.Or_testContext):
        pass


    # Enter a parse tree produced by Python2Parser#and_test.
    def enterAnd_test(self, ctx:Python2Parser.And_testContext):
        pass

    # Exit a parse tree produced by Python2Parser#and_test.
    def exitAnd_test(self, ctx:Python2Parser.And_testContext):
        pass


    # Enter a parse tree produced by Python2Parser#not_test.
    def enterNot_test(self, ctx:Python2Parser.Not_testContext):
        pass

    # Exit a parse tree produced by Python2Parser#not_test.
    def exitNot_test(self, ctx:Python2Parser.Not_testContext):
        pass


    # Enter a parse tree produced by Python2Parser#comparison.
    def enterComparison(self, ctx:Python2Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by Python2Parser#comparison.
    def exitComparison(self, ctx:Python2Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by Python2Parser#comp_op.
    def enterComp_op(self, ctx:Python2Parser.Comp_opContext):
        pass

    # Exit a parse tree produced by Python2Parser#comp_op.
    def exitComp_op(self, ctx:Python2Parser.Comp_opContext):
        pass


    # Enter a parse tree produced by Python2Parser#expr.
    def enterExpr(self, ctx:Python2Parser.ExprContext):
        pass

    # Exit a parse tree produced by Python2Parser#expr.
    def exitExpr(self, ctx:Python2Parser.ExprContext):
        pass


    # Enter a parse tree produced by Python2Parser#xor_expr.
    def enterXor_expr(self, ctx:Python2Parser.Xor_exprContext):
        pass

    # Exit a parse tree produced by Python2Parser#xor_expr.
    def exitXor_expr(self, ctx:Python2Parser.Xor_exprContext):
        pass


    # Enter a parse tree produced by Python2Parser#and_expr.
    def enterAnd_expr(self, ctx:Python2Parser.And_exprContext):
        pass

    # Exit a parse tree produced by Python2Parser#and_expr.
    def exitAnd_expr(self, ctx:Python2Parser.And_exprContext):
        pass


    # Enter a parse tree produced by Python2Parser#shift_expr.
    def enterShift_expr(self, ctx:Python2Parser.Shift_exprContext):
        pass

    # Exit a parse tree produced by Python2Parser#shift_expr.
    def exitShift_expr(self, ctx:Python2Parser.Shift_exprContext):
        pass


    # Enter a parse tree produced by Python2Parser#arith_expr.
    def enterArith_expr(self, ctx:Python2Parser.Arith_exprContext):
        pass

    # Exit a parse tree produced by Python2Parser#arith_expr.
    def exitArith_expr(self, ctx:Python2Parser.Arith_exprContext):
        pass


    # Enter a parse tree produced by Python2Parser#term.
    def enterTerm(self, ctx:Python2Parser.TermContext):
        pass

    # Exit a parse tree produced by Python2Parser#term.
    def exitTerm(self, ctx:Python2Parser.TermContext):
        pass


    # Enter a parse tree produced by Python2Parser#factor.
    def enterFactor(self, ctx:Python2Parser.FactorContext):
        pass

    # Exit a parse tree produced by Python2Parser#factor.
    def exitFactor(self, ctx:Python2Parser.FactorContext):
        pass


    # Enter a parse tree produced by Python2Parser#power.
    def enterPower(self, ctx:Python2Parser.PowerContext):
        pass

    # Exit a parse tree produced by Python2Parser#power.
    def exitPower(self, ctx:Python2Parser.PowerContext):
        pass


    # Enter a parse tree produced by Python2Parser#atom.
    def enterAtom(self, ctx:Python2Parser.AtomContext):
        pass

    # Exit a parse tree produced by Python2Parser#atom.
    def exitAtom(self, ctx:Python2Parser.AtomContext):
        pass


    # Enter a parse tree produced by Python2Parser#listmaker.
    def enterListmaker(self, ctx:Python2Parser.ListmakerContext):
        pass

    # Exit a parse tree produced by Python2Parser#listmaker.
    def exitListmaker(self, ctx:Python2Parser.ListmakerContext):
        pass


    # Enter a parse tree produced by Python2Parser#testlist_comp.
    def enterTestlist_comp(self, ctx:Python2Parser.Testlist_compContext):
        pass

    # Exit a parse tree produced by Python2Parser#testlist_comp.
    def exitTestlist_comp(self, ctx:Python2Parser.Testlist_compContext):
        pass


    # Enter a parse tree produced by Python2Parser#lambdef.
    def enterLambdef(self, ctx:Python2Parser.LambdefContext):
        pass

    # Exit a parse tree produced by Python2Parser#lambdef.
    def exitLambdef(self, ctx:Python2Parser.LambdefContext):
        pass


    # Enter a parse tree produced by Python2Parser#trailer.
    def enterTrailer(self, ctx:Python2Parser.TrailerContext):
        pass

    # Exit a parse tree produced by Python2Parser#trailer.
    def exitTrailer(self, ctx:Python2Parser.TrailerContext):
        pass


    # Enter a parse tree produced by Python2Parser#subscriptlist.
    def enterSubscriptlist(self, ctx:Python2Parser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by Python2Parser#subscriptlist.
    def exitSubscriptlist(self, ctx:Python2Parser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by Python2Parser#subscript.
    def enterSubscript(self, ctx:Python2Parser.SubscriptContext):
        pass

    # Exit a parse tree produced by Python2Parser#subscript.
    def exitSubscript(self, ctx:Python2Parser.SubscriptContext):
        pass


    # Enter a parse tree produced by Python2Parser#sliceop.
    def enterSliceop(self, ctx:Python2Parser.SliceopContext):
        pass

    # Exit a parse tree produced by Python2Parser#sliceop.
    def exitSliceop(self, ctx:Python2Parser.SliceopContext):
        pass


    # Enter a parse tree produced by Python2Parser#exprlist.
    def enterExprlist(self, ctx:Python2Parser.ExprlistContext):
        pass

    # Exit a parse tree produced by Python2Parser#exprlist.
    def exitExprlist(self, ctx:Python2Parser.ExprlistContext):
        pass


    # Enter a parse tree produced by Python2Parser#testlist.
    def enterTestlist(self, ctx:Python2Parser.TestlistContext):
        pass

    # Exit a parse tree produced by Python2Parser#testlist.
    def exitTestlist(self, ctx:Python2Parser.TestlistContext):
        pass


    # Enter a parse tree produced by Python2Parser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:Python2Parser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by Python2Parser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:Python2Parser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by Python2Parser#classdef.
    def enterClassdef(self, ctx:Python2Parser.ClassdefContext):
        pass

    # Exit a parse tree produced by Python2Parser#classdef.
    def exitClassdef(self, ctx:Python2Parser.ClassdefContext):
        pass


    # Enter a parse tree produced by Python2Parser#arglist.
    def enterArglist(self, ctx:Python2Parser.ArglistContext):
        pass

    # Exit a parse tree produced by Python2Parser#arglist.
    def exitArglist(self, ctx:Python2Parser.ArglistContext):
        pass


    # Enter a parse tree produced by Python2Parser#argument.
    def enterArgument(self, ctx:Python2Parser.ArgumentContext):
        pass

    # Exit a parse tree produced by Python2Parser#argument.
    def exitArgument(self, ctx:Python2Parser.ArgumentContext):
        pass


    # Enter a parse tree produced by Python2Parser#list_iter.
    def enterList_iter(self, ctx:Python2Parser.List_iterContext):
        pass

    # Exit a parse tree produced by Python2Parser#list_iter.
    def exitList_iter(self, ctx:Python2Parser.List_iterContext):
        pass


    # Enter a parse tree produced by Python2Parser#list_for.
    def enterList_for(self, ctx:Python2Parser.List_forContext):
        pass

    # Exit a parse tree produced by Python2Parser#list_for.
    def exitList_for(self, ctx:Python2Parser.List_forContext):
        pass


    # Enter a parse tree produced by Python2Parser#list_if.
    def enterList_if(self, ctx:Python2Parser.List_ifContext):
        pass

    # Exit a parse tree produced by Python2Parser#list_if.
    def exitList_if(self, ctx:Python2Parser.List_ifContext):
        pass


    # Enter a parse tree produced by Python2Parser#comp_iter.
    def enterComp_iter(self, ctx:Python2Parser.Comp_iterContext):
        pass

    # Exit a parse tree produced by Python2Parser#comp_iter.
    def exitComp_iter(self, ctx:Python2Parser.Comp_iterContext):
        pass


    # Enter a parse tree produced by Python2Parser#comp_for.
    def enterComp_for(self, ctx:Python2Parser.Comp_forContext):
        pass

    # Exit a parse tree produced by Python2Parser#comp_for.
    def exitComp_for(self, ctx:Python2Parser.Comp_forContext):
        pass


    # Enter a parse tree produced by Python2Parser#comp_if.
    def enterComp_if(self, ctx:Python2Parser.Comp_ifContext):
        pass

    # Exit a parse tree produced by Python2Parser#comp_if.
    def exitComp_if(self, ctx:Python2Parser.Comp_ifContext):
        pass


    # Enter a parse tree produced by Python2Parser#testlist1.
    def enterTestlist1(self, ctx:Python2Parser.Testlist1Context):
        pass

    # Exit a parse tree produced by Python2Parser#testlist1.
    def exitTestlist1(self, ctx:Python2Parser.Testlist1Context):
        pass


    # Enter a parse tree produced by Python2Parser#encoding_decl.
    def enterEncoding_decl(self, ctx:Python2Parser.Encoding_declContext):
        pass

    # Exit a parse tree produced by Python2Parser#encoding_decl.
    def exitEncoding_decl(self, ctx:Python2Parser.Encoding_declContext):
        pass


    # Enter a parse tree produced by Python2Parser#yield_expr.
    def enterYield_expr(self, ctx:Python2Parser.Yield_exprContext):
        pass

    # Exit a parse tree produced by Python2Parser#yield_expr.
    def exitYield_expr(self, ctx:Python2Parser.Yield_exprContext):
        pass



del Python2Parser