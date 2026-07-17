/* 9421FFF0 */    stwu r1, -0x10(r1)
/* 7C0802A6 */     mflr r0
/* 90010014 */    stw r0, 0x14(r1)
/* 93E1000c */    stw r31, 0xc(r1)
/* 93C10008 */    stw r30, 0x8(r1)
/* 7C7E1b78 */    mr r30, r3
/* 7C9F2378 */    mr r31, r4
/* 4B904B4D */    bl vsnprintf
/* 38000000 */    li r0, 0x0
/* 7C9FF214 */    add r4, r31, r30
/* 9804FFFF */    stb r0, -0x1(r4)
/* 83E1000C */    lwz r31, 0xc(r1)
/* 83C10008 */   lwz r30, 0x8(r1)
/* 80010014 */    lwz r0, 0x14(r1)
/* 7C0803A6 */    mtlr r0
/* 38210010 */    addi r1, r1, 0x10
/* 4E800020 */    blr