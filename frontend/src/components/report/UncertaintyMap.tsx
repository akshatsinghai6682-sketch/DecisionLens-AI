import React from 'react';
import { Layers, Eye, EyeOff } from 'lucide-react';

interface UncertaintyMapProps {
  knownFactors: Array<{ factor: string; confidence: number }>;
  unknownFactors: Array<{ factor: string; impact: string }>;
  assumptions: string[];
}

export const UncertaintyMap: React.FC<UncertaintyMapProps> = ({
  knownFactors,
  unknownFactors,
  assumptions,
}) => {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 space-y-6">
      <div>
        <div className="flex items-center gap-2 mb-4">
          <Eye className="text-green-600" size={24} />
          <h3 className="text-lg font-bold text-gray-900">Known Factors</h3>
        </div>
        <div className="space-y-2">
          {knownFactors.map((item, idx) => (
            <div key={idx} className="p-3 bg-green-50 rounded border border-green-200">
              <p className="text-sm font-medium text-gray-900">{item.factor}</p>
              <div className="mt-2 bg-green-200 rounded h-2 overflow-hidden">
                <div
                  className="bg-green-600 h-full"
                  style={{ width: `${item.confidence * 100}%` }}
                ></div>
              </div>
              <p className="text-xs text-gray-600 mt-1">{Math.round(item.confidence * 100)}% confident</p>
            </div>
          ))}
        </div>
      </div>

      <div>
        <div className="flex items-center gap-2 mb-4">
          <EyeOff className="text-red-600" size={24} />
          <h3 className="text-lg font-bold text-gray-900">Unknown Factors</h3>
        </div>
        <div className="space-y-2">
          {unknownFactors.map((item, idx) => (
            <div key={idx} className="p-3 bg-red-50 rounded border border-red-200">
              <p className="text-sm font-medium text-gray-900">{item.factor}</p>
              <p className="text-xs text-red-600 font-semibold mt-1">Impact: {item.impact.toUpperCase()}</p>
            </div>
          ))}
        </div>
      </div>

      <div>
        <div className="flex items-center gap-2 mb-4">
          <Layers className="text-blue-600" size={24} />
          <h3 className="text-lg font-bold text-gray-900">Key Assumptions</h3>
        </div>
        <div className="space-y-2">
          {assumptions.map((assumption, idx) => (
            <div key={idx} className="p-3 bg-blue-50 rounded border border-blue-200">
              <p className="text-sm text-gray-900">• {assumption}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
