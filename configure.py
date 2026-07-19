import argparse
import sys
# from pathlib import Path
from tools.project import (
    Function,
    Config,
    NoProgress,
    WorkInProgress,
    Done,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "mode",
    choices=["configure", "generate"],
    default="configure",
    help="Script mode (configure (default), generate)",
    nargs="?"
)
args = parser.parse_args()

MaxFunc = 1392

config = Config()

config.setFunctions(MaxFunc, [
    Function(
        NoProgress,
        "app::AppImpl::AppImpl(app::System&)",
        "80175AAC - AppImpl__AppImpl",
    ),
    Function(
        NoProgress,
        "app::AppImpl::run(bool)",
        "80176370 - AppImpl__run"
    ),
    Function(
        NoProgress,
        "app::AppImpl::runWithRootSequence(std::auto_ptr<seq::ISequence>)",
        "80176734 - AppImpl__runWithRootSequence",
    ),
    Function(
        NoProgress,
        "app::AppImpl::enterSceneSequence(seq::ISequence&)",
        "80176A34 - AppImpl__enterSceneSequence",
    ),
    Function(
        NoProgress,
        "app::AppImpl::onBeforeSceneCreate(void)",
        "80176D64 - AppImpl__onBeforeSceneCreate",
    ),
    Function(
        NoProgress,
        "app::AppImpl::sceneLoop(scn::IScene &)",
        "80176F48 - AppImpl__sceneLoop",
    ),
    Function(
        NoProgress,
        "app::AppImpl::onSceneStartProcess(scn::IScene &)",
        "80177114 - AppImpl__onSceneStartProcess",
    ),
    Function(
        Done,
        "scn::step::hero::AbilityManager::setUseCount(unsigned long)",
        "804D1F84 - AbilityManager__setUseCount",
    ),
    Function(
        Done,
        "scn::step::hero::AbilityManager::canSuperBGMRequest() const",
        "804D2904 - AbilityManager__canSuperBGMRequest",
    ),
    Function(
        Done,
        "scn::step::hero::Counter::killEnemyCount() const",
        "804DE1A0 - Counter__killEnemyCount",
    ),
    Function(
        Done,
        "scn::step::info::HeroStatusIcon::startDamageAnim()",
        "805CC870 - HeroStatusIcon__startDamageAnim",
    ),
    Function(
        Done,
        "scn::step::vacuum::Attacker::setGimmickInterval(unsigned long)",
        "80607728 - Attacker_setGimmickInterval",
    ),
    Function(
        Done,
        "scn::subgame::common::boxmenu::SelectableBox::setFixSELabel(unsigned long)",
        "8067F4DC - SelectableBox__setFixSELabel",
    ),
    Function(
        Done,
        "util::StringFormatV(char*, unsigned long, const char*, __va_list_struct*)",
        "80708A44 - StringFormatV",
    ),
])

if args.mode == "configure":
    config.progressReport()
elif args.mode == "generate":
    config.generate()
else:
    sys.exit("Unknown mode: " + args.mode)
