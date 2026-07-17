/* 9421FFF0 */ stwu r1, -0x10(r1)
/* 7C0802A6 */ mflr r0
/* 90010014 */ stw r0, 0x14(r1)
/* 80630000 */ lwz r3,0x0(r3)
/* 4803CD05 */ bl scn::step::hero::Utility::IsFinalBattle
/* 7c600034 */ cntlzw r0, r3
/* 5403D97E */ srwi r3, r0, 5 (rlwinm r3, r0, 27, 5, 31)
/* 80010014 */ lwz r0, 0x14(r1)
/* 7C0803A6 */ mtlr r0
/* 38210010 */ addi r1, r1, 0x10
/* 4E800020 */ blr