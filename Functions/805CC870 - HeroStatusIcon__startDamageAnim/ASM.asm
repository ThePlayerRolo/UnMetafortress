/* 9421FFF0 */	stwu r1, -0x10(r1)
/* 7C0802A6 */	mflr r0
/* 90010014 */	stw r0, 0x14(r1)
/* 93E1000C */	stw r31, 0xc(r1)
/* 7C7F1B78 */	mr r31, r3
/* 806306A8 */	lwz r3, 0x6A8(r3)
/* 388DF02C */	li r4, lbl_8055B59C@sda21
/* 4BBEBCC1 */	bl setAnimByName__Q23lyt6LayoutFPCc
/* 807F06A8 */	lwz r3, 0x6A8(r31)
/* 38800000 */	li r4, 0x0
/* 4BBEBE69 */	bl start__Q23lyt6LayoutFb
/* 7FE3FB78 */	mr r3, r31
/* 48000315 */	bl stopPinchAnim__Q43scn4step4info14HeroStatusIconFv
/* 83E1000C */	lwz r31, 0xc(r1)
/* 80010014 */	lwz r0, 0x14(r1)
/* 7C0803A6 */	mtlr r0
/* 38210010 */	addi r1, r1, 0x10
/* 4E800020 */	blr