import FWCore.ParameterSet.Config as cms

import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
#
# When starting from recHits, there are of course no "regional digis" and no "regional rechits".
# In order not to duplicate too much the modules in the Egamma paths, we define
# here the modules "ecalRegionalEgammaWeightUncalibRecHit", "ecalRegionalEgammaRecHit" etc..
# and the sequences ecalRegionalEgammaRecoSequence etc..
# This way, the subsequent clustering modules always start from the RecHits created
# by "ecalRegionalEgammaRecHit", both in the "FromDigis", the "FromRaw" and 
# the "FromRecHits" cases.
#
#
# From here on simply cloning ecalLocalRecoSequence.cff
#   with updated InputTags
#
hltEcalRegionalEgammaRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalRegionalMuonsRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalRegionalTausRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalRegionalJetsRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalRecHitAll = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()

