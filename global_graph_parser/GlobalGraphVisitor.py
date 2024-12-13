# Generated from GlobalGraph.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GlobalGraphParser import GlobalGraphParser
else:
    from GlobalGraphParser import GlobalGraphParser

# This class defines a complete generic visitor for a parse tree produced by GlobalGraphParser.

class GlobalGraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GlobalGraphParser#init.
    def visitInit(self, ctx:GlobalGraphParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#fork.
    def visitFork(self, ctx:GlobalGraphParser.ForkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#loop.
    def visitLoop(self, ctx:GlobalGraphParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#sequential.
    def visitSequential(self, ctx:GlobalGraphParser.SequentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#interaction.
    def visitInteraction(self, ctx:GlobalGraphParser.InteractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#choice.
    def visitChoice(self, ctx:GlobalGraphParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GlobalGraphParser#parenthesis.
    def visitParenthesis(self, ctx:GlobalGraphParser.ParenthesisContext):
        return self.visitChildren(ctx)



del GlobalGraphParser