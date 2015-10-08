/************************************************************************************
 * WrightEagle (Soccer Simulation League 2D)                                        *
 * BASE SOURCE CODE RELEASE 2013                                                    *
 * Copyright (c) 1998-2013 WrightEagle 2D Soccer Simulation Team,                   *
 *                         Multi-Agent Systems Lab.,                                *
 *                         School of Computer Science and Technology,               *
 *                         University of Science and Technology of China            *
 * All rights reserved.                                                             *
 *                                                                                  *
 * Redistribution and use in source and binary forms, with or without               *
 * modification, are permitted provided that the following conditions are met:      *
 *     * Redistributions of source code must retain the above copyright             *
 *       notice, this list of conditions and the following disclaimer.              *
 *     * Redistributions in binary form must reproduce the above copyright          *
 *       notice, this list of conditions and the following disclaimer in the        *
 *       documentation and/or other materials provided with the distribution.       *
 *     * Neither the name of the WrightEagle 2D Soccer Simulation Team nor the      *
 *       names of its contributors may be used to endorse or promote products       *
 *       derived from this software without specific prior written permission.      *
 *                                                                                  *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND  *
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED    *
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE           *
 * DISCLAIMED. IN NO EVENT SHALL WrightEagle 2D Soccer Simulation Team BE LIABLE    *
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL       *
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR       *
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER       *
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,    *
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF *
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                *
 ************************************************************************************/

#ifndef __BehaviorPass_H__
#define __BehaviorPass_H__

#include "BehaviorBase.h"
#include "VisualSystem.h"
#include <vector>

class BehaviorPassExecuter: public BehaviorExecuterBase<BehaviorAttackData>
{
public:
    BehaviorPassExecuter(Agent &agent);
    virtual ~BehaviorPassExecuter(void);

    bool Execute(const ActiveBehavior & act_bhv);
    void SubmitVisualRequest(const ActiveBehavior & pass, double plus = 0.0) {
    	if (pass.mKickCycle == 1) {
    		VisualSystem::instance().RaisePlayer(mAgent, pass.mKeyTm.mUnum, 3.0 + plus);
    		VisualSystem::instance().RaisePlayer(mAgent, -pass.mKeyOppGB.mUnum, 3.0 + plus);
    		VisualSystem::instance().RaisePlayer(mAgent, -pass.mKeyOppGT.mUnum, 3.0 + plus);
    	}
    	else {
    		VisualSystem::instance().RaisePlayer(mAgent, pass.mKeyTm.mUnum, 2.0 + plus);
    		VisualSystem::instance().RaisePlayer(mAgent, -pass.mKeyOppGB.mUnum, 3.0 + plus);
    		VisualSystem::instance().RaisePlayer(mAgent, -pass.mKeyOppGT.mUnum, 2.0 + plus);
    	}
    }

    static const BehaviorType BEHAVIOR_TYPE;
};

class BehaviorPassPlanner : public BehaviorPlannerBase<BehaviorAttackData> {
public:
	BehaviorPassPlanner(Agent &agent);
	virtual ~BehaviorPassPlanner(void);

	void Plan(std::list<ActiveBehavior> & behavior_list);
};

#endif

