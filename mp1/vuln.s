	.file	"vuln.c"
	.intel_syntax noprefix
# GNU C17 (Ubuntu 9.4.0-1ubuntu1~20.04.2) version 9.4.0 (x86_64-linux-gnu)
#	compiled by GNU C version 9.4.0, GMP version 6.2.0, MPFR version 4.0.2, MPC version 1.1.0, isl version isl-0.22.1-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -imultilib 32 -imultiarch i386-linux-gnu vuln.c -m32
# -masm=intel -mtune=generic -march=i686 -Og -w -fno-stack-protector
# -fno-pie -fverbose-asm -fasynchronous-unwind-tables -Wformat
# -Wformat-security -fstack-clash-protection -fcf-protection
# options enabled:  -faggressive-loop-optimizations -fassume-phsa
# -fasynchronous-unwind-tables -fauto-inc-dec -fcombine-stack-adjustments
# -fcommon -fcompare-elim -fcprop-registers -fdefer-pop
# -fdelete-null-pointer-checks -fdwarf2-cfi-asm -fearly-inlining
# -feliminate-unused-debug-types -fforward-propagate
# -ffp-int-builtin-inexact -ffunction-cse -fgcse-lm -fgnu-runtime
# -fgnu-unique -fguess-branch-probability -fident -finline -finline-atomics
# -fipa-profile -fipa-pure-const -fipa-reference
# -fipa-reference-addressable -fipa-stack-alignment -fira-hoist-pressure
# -fira-share-save-slots -fira-share-spill-slots -fivopts
# -fkeep-static-consts -fleading-underscore -flifetime-dse
# -flto-odr-type-merging -fmath-errno -fmerge-constants
# -fmerge-debug-strings -fomit-frame-pointer -fpcc-struct-return -fpeephole
# -fplt -fprefetch-loop-arrays -freorder-blocks
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
# -fshow-column -fshrink-wrap -fshrink-wrap-separate -fsigned-zeros
# -fsplit-ivs-in-unroller -fsplit-wide-types -fssa-backprop
# -fstack-clash-protection -fstdarg-opt -fstrict-volatile-bitfields
# -fsync-libcalls -ftoplevel-reorder -ftrapping-math
# -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars
# -ftree-copy-prop -ftree-cselim -ftree-dce -ftree-dominator-opts
# -ftree-dse -ftree-forwprop -ftree-fre -ftree-loop-if-convert
# -ftree-loop-im -ftree-loop-ivcanon -ftree-loop-optimize
# -ftree-parallelize-loops= -ftree-phiprop -ftree-reassoc -ftree-scev-cprop
# -ftree-sink -ftree-slsr -ftree-ter -funit-at-a-time -funwind-tables
# -fverbose-asm -fzero-initialized-in-bss -m32 -m80387 -m96bit-long-double
# -malign-stringops -mavx256-split-unaligned-load
# -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387 -mglibc
# -mieee-fp -mlong-double-80 -mno-red-zone -mno-sse4 -mpush-args -msahf
# -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.globl	vuln
	.type	vuln, @function
vuln:
.LFB23:
	.cfi_startproc
	endbr32	
	sub	esp, 40	#,
	.cfi_def_cfa_offset 44
# vuln.c:6:     gets(buffer);
	lea	eax, [esp+20]	# tmp82,
	push	eax	# tmp82
	.cfi_def_cfa_offset 48
	call	gets	#
# vuln.c:7: }
	add	esp, 44	#,
	.cfi_def_cfa_offset 4
	ret	
	.cfi_endproc
.LFE23:
	.size	vuln, .-vuln
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	endbr32	
	push	ebp	#
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp	#,
	.cfi_def_cfa_register 5
	and	esp, -16	#,
# vuln.c:10:     vuln();
	call	vuln	#
.L4:
	jmp	.L4	#
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 4
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 4
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 4
4:
